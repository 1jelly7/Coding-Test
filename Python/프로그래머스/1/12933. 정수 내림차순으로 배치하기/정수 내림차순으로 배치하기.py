def solution(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    
    return int(''.join(sorted(str(n), reverse=True)))