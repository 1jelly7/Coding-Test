def solution(a, b):
    odd_count = (a % 2 == 1) + (b % 2 == 1)
    
    if odd_count == 2:
        return a**2 + b**2
    if odd_count == 1:
        return 2 * (a + b)
    if odd_count == 0:
        return abs(a - b)