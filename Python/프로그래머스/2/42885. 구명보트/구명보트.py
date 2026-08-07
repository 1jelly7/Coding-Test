def solution(people, limit):
    # Sort people by weight so we can always try the lightest and the heaviest together.
    people.sort()

    left, right = 0, len(people) - 1
    boats = 0

    # Use a two-pointer greedy strategy.
    while left <= right:
        # The heaviest person always takes a boat.
        # If the lightest person can share the boat, move both pointers.
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats