def solution(a, b):
    score = (a % 2 != 0) + (b % 2 != 0)
    
    if score == 2:
        return a ** 2 + b ** 2
    if score == 1:
        return 2 * (a + b)
    if score == 0:
        return abs(a - b)