def solution(n):
    return sum(1 for num in range(1, n + 1) if n % num == 0)