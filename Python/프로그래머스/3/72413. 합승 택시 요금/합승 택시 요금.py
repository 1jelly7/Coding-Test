from typing import List

INF = float("inf")


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    if n < 3:
        raise ValueError(f"n must be >= 3, got {n}")
    if not (1 <= s <= n and 1 <= a <= n and 1 <= b <= n):
        raise ValueError(
            f"s, a, b must all be within [1, {n}], got s={s}, a={a}, b={b}"
        )
    if len({s, a, b}) != 3:
        raise ValueError(f"s, a, b must all be distinct, got s={s}, a={a}, b={b}")

    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for edge in fares:
        if len(edge) != 3:
            raise ValueError(f"Each fare entry must be [c, d, f], got {edge}")

        c, d, f = edge

        if not (1 <= c <= n and 1 <= d <= n):
            raise ValueError(f"Fare endpoints must be within [1, {n}], got {edge}")
        if f <= 0:
            raise ValueError(f"Fare must be a positive number, got {edge}")
        
        if f < dist[c][d]:
            dist[c][d] = f
            dist[d][c] = f
    
    for k in range(1, n + 1):
        dist_k = dist[k]
        for i in range(1, n + 1):
            dist_i = dist[i]
            dik = dist_i[k]
            if dik == INF:
                continue
            for j in range(1, n + 1):
                new_cost = dik + dist_k[j]
                if new_cost < dist_i[j]:
                    dist_i[j] = new_cost

    best_total = INF
    for p in range(1, n + 1):
        shared_leg = dist[s][p]
        if shared_leg == INF:
            continue

        a_leg = dist[p][a]
        b_leg = dist[p][b]
        if a_leg == INF or b_leg == INF:
            continue

        total = shared_leg + a_leg + b_leg
        if total < best_total:
            best_total = total
    
    if best_total == INF:
        raise ValueError("No valid route found connecting s, a, and b.")

    return int(best_total)