def solution(n):
    count = 1
    for start in range(1, (n + 1) // 2):
        sum = start
        for end in range(start + 1, (n + 1) // 2 + 1):
            sum += end
            if sum == n:
                count += 1
                break
            elif sum > n:
                break
    
    return count