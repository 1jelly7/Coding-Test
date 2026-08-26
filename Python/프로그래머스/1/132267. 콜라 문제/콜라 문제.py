def solution(a: int, b: int, n: int) -> int:
    total = 0
    empty = n
    
    if any(isinstance(value, bool) or not isinstance(value, int)
           for value in (a, b, n)):
        raise TypeError("a, b, and n must all be integers.")
    
    if b < 1:
        raise ValueError("b must be at least 1.")
    
    if a <= b:
        raise ValueError("a must be greater than b.")
    
    if n < a:
        raise ValueError("n must be greater than or equal to a.")

    while empty >= a:
        received = empty // a * b

        total += received

        remaining = empty % a

        empty = remaining + received

    return total