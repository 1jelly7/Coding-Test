def solution(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    return [int(d) for d in str(n)[::-1]]