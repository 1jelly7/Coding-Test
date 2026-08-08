def solution(a, b):
    start, end = (a, b) if b > a else (b, a)
    
    return sum(range(start, end + 1))