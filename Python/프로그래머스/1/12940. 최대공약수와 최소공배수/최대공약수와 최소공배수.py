def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    
    return a

def lcm(a: int, b: int, gcd: int) -> int:
    return a * b // gcd
    

def solution(n, m):
    if n < 1 or m < 1:
        raise ValueError("n and m must be positive integers")
    
    g = gcd(m, n)
    l = lcm(m, n, g)
    
    return [g, l]