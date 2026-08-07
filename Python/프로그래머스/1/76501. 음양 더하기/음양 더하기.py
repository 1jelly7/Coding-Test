def solution(absolutes, signs):
    if len(absolutes) != len(signs):
        return 0
    
    total = 0
    
    for value, is_positive in zip(absolutes, signs):
        total += value if is_positive else -value
    
    return total