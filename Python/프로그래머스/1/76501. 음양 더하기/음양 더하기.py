def solution(absolutes, signs):
    if len(absolutes) != len(signs):
        raise ValueError("absolutes and signs must have the same length")
    
    total = 0
    
    for value, is_positive in zip(absolutes, signs):
        if not isinstance(value, int) or value < 0:
            raise ValueError("absolutes must contain non-negative integers")
        
        total += value if is_positive else -value
    
    return total