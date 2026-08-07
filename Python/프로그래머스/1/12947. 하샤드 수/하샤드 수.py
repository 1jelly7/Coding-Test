def solution(x):
    tmp = x
    total = 0
    
    while tmp > 0:
        total += tmp % 10
        tmp //= 10
    
    return x % total == 0