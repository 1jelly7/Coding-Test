"""
PROBLEM SUMMARY
---------------
There are `n` locations (numbered 1…n).
Two people (A and B) start together at location `s`
and need to reach their own destinations `a` and `b`.
They may ride together for part of the trip, then split up,
and each take their own taxi for the rest of the way.
We want the MINIMUM TOTAL fare paid by both of them combined.

We are given a weighted, undirected graph `fares`, where each entry
[c, d, f] means "the taxi fare between location c and location d is f,
and it costs the same in both directions".

We need to find the minimum total cost such that:
    cost(s -> meeting_point) + cost(meeting_point -> a) + cost(meeting_point -> b)
is minimized, where `meeting_point` can be ANY node (including s itself,
which represents "no carpooling at all", or a/b themselves).

APPROACH
--------
Since n <= 200, an O(n^3) All-Pairs Shortest Path algorithm (Floyd-Warshall)
is perfectly fast enough (200^3 = 8,000,000 basic operations, well within time limits).

Steps:
1. Build an n x n cost matrix, initialized to "infinity" for all pairs
   except a node to itself (cost 0), then fill in the direct fares given.
2. Run Floyd-Warshall to compute the shortest path between EVERY pair of nodes.
   After this step, dist[i][j] = the cheapest fare to go from i to j,
   possibly by passing through other nodes.
3. Try every node `k` (1…n) as the possible "split point" where A and B part ways, and compute:
       total = dist[s][k] + dist[k][a] + dist[k][b]
   The minimum such `total` over all k is the answer.
   (k = s naturally covers the "never carpool" case, since dist[s][s] = 0.)

COMPLEXITY
----------
Time:  O(n^3) -- Floyd-Warshall triple loop. (n <= 200 -> at most 8,000,000 iterations)
Space: O(n^2) -- the distance matrix.
"""

from typing import List

# A sentinel value representing "no route currently known between two nodes".
# It must be larger than any real path cost.
# Using Python's float('inf') keeps comparisons and additions simple and correct.
# No risk of accidental integer overflow, unlike picking some large int.
INF = float("inf")


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    """
    Compute the minimum total taxi fare for A and B to each reach their
    destinations, starting together from `s`, optionally sharing part
    of the ride.

    Args:
        n: Number of locations, labeled 1…n.
        s: Starting location for both A and B.
        a: A's destination.
        b: B's destination.
        fares: List of [c, d, f] triples meaning the fare between
               location c and location d (valid in both directions) is f.

    Returns:
        The minimum total fare as an integer.

    Raises:
        ValueError: If the input violates the documented constraints.
    """

    # ---- 1. Defensive input validation ---------------------------------
    # Production code shouldn't blindly trust its inputs.
    # These checks fail fast with a clear error message instead of silently returning
    # a wrong answer or crashing later with a confusing IndexError.
    if n < 3:
        raise ValueError(f"n must be >= 3, got {n}")
    if not (1 <= s <= n and 1 <= a <= n and 1 <= b <= n):
        raise ValueError(
            f"s, a, b must all be within [1, {n}], got s={s}, a={a}, b={b}"
        )
    if len({s, a, b}) != 3:
        raise ValueError(f"s, a, b must all be distinct, got s={s}, a={a}, b={b}")

    # ---- 2. Build the initial distance matrix --------------------------
    # We use 1-based indexing throughout (row/column 0 is simply unused),
    # so location numbers map directly onto matrix indices without extra -1 / +1 bookkeeping.
    # This trades a tiny bit of memory for much easier-to-read code -- a good trade-off for n <= 200.
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # The distance from any node to itself is always 0 (no taxi needed).
    for i in range(1, n + 1):
        dist[i][i] = 0

    # Fill in the direct fares given in the input.
    # The graph is undirected, so a single entry updates both dist[c][d] and dist[d][c].
    for edge in fares:
        # Defensive check: each fare entry must be exactly [c, d, f].
        if len(edge) != 3:
            raise ValueError(f"Each fare entry must be [c, d, f], got {edge}")

        c, d, f = edge

        if not (1 <= c <= n and 1 <= d <= n):
            raise ValueError(f"Fare endpoints must be within [1, {n}], got {edge}")
        if f <= 0:
            raise ValueError(f"Fare must be a positive number, got {edge}")

        # If duplicate edges were ever present, keep the cheaper one rather than blindly overwriting.
        if f < dist[c][d]:
            dist[c][d] = f
            dist[d][c] = f

    # ---- 3. Floyd-Warshall: all-pairs shortest path ---------------------
    # After this triple loop finishes, dist[i][j] holds the cheapest possible fare to travel from i to j,
    # potentially passing through any number of intermediate nodes.
    # Classic Floyd-Warshall recurrence, read as:
    #   "Is it cheaper to go i -> j directly, or i -> k -> j?"
    #   dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for k in range(1, n + 1):
        # Cache row k once per outer iteration.
        # Repeated list indexing (dist[k][j] on every inner-loop step) is surprisingly costly in Python,
        # so caching the row reference is a simple, safe speedup.
        dist_k = dist[k]
        for i in range(1, n + 1):
            dist_i = dist[i]
            dik = dist_i[k]
            # If I can't even reach k, there's no point checking any j -- skip the whole inner loop early.
            # This is a cheap but meaningful optimization on sparse-ish graphs.
            if dik == INF:
                continue
            for j in range(1, n + 1):
                new_cost = dik + dist_k[j]
                if new_cost < dist_i[j]:
                    dist_i[j] = new_cost

    # ---- 4. Try every possible "split point" ----------------------------
    # For each candidate node p, imagine A and B share one taxi from s to p,
    # then go their separate ways: p -> a for A, and p -> b for B.
    # p = s is automatically included in this loop and represents
    # "no carpooling at all" (since dist[s][s] == 0).
    best_total = INF
    for p in range(1, n + 1):
        shared_leg = dist[s][p]
        if shared_leg == INF:
            continue  # p is unreachable from s -- not a valid split point

        a_leg = dist[p][a]
        b_leg = dist[p][b]
        if a_leg == INF or b_leg == INF:
            continue  # can't reach a or b from this particular split point

        total = shared_leg + a_leg + b_leg
        if total < best_total:
            best_total = total

    if best_total == INF:
        raise ValueError("No valid route found connecting s, a, and b.")

    return int(best_total)
