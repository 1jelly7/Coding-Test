def solution(n):
    count = 1  # n = n
    left, right = 1, 1
    total = 1
    
    while left < n:
        if total == n:
            count += 1
            total -= left
            left += 1
        elif total < n:
            right += 1
            total += right
        else:  # total > n
            total -= left
            left += 1
    
    return count