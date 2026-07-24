def solution(n):
    # Count the representation using n itself as a single number.
    count = 1
    # Sliding window boundaries: current sequence is [left, right].
    left, right = 1, 1
    # Sum of numbers from left to right
    total = 1
    
    while left < n:
        if total == n:
            # If the sum matches n, we found one valid representation.
            count += 1
            # Shrink the window from the left to look for the next possibility.
            total -= left
            left += 1
        elif total < n:
            # If the sum is too small, expand the window to the right.
            right += 1
            total += right
        else:  # total > n
            # If the sum is too large, shrink the window from the left.
            total -= left
            left += 1
    
    return count