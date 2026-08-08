def solution(a, b):    
    try:
        iter(a)
        iter(b)
    except TypeError:
        raise TypeError("Both a and b must be iterable")
    
    if len(a) != len(b):
        raise ValueError("a and b must have the same length")
    
    return sum(x * y for x, y in zip(a, b))