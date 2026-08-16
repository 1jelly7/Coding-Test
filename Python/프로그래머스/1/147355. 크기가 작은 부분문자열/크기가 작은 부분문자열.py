def solution(t, p):    
    if not (isinstance(t, str) and isinstance(p, str)):
        raise ValueError("t and p must be strings")
    
    if not (t.isdigit() and p.isdigit()):
        raise ValueError("t and p must contain digits only")
    
    window_size = len(p)
    count = 0
    
    for start in range(len(t) - len(p) + 1):
        if t[start : start + window_size] <= p:
            count += 1
    
    return count