import math

def solution(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    
    divisors = set()
    
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    
    return sorted(divisors)