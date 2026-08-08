def solution(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total