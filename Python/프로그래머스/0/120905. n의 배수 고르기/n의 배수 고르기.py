def solution(n, numlist):    
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    
    if any(not isinstance(value, int) or isinstance(value, bool)
           for value in numlist):
        raise TypeError("Every element in numlist must be an integer.")
    
    return [value for value in numlist if value % n == 0]