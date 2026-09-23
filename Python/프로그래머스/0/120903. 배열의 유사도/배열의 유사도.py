def solution(s1, s2):
    same_count = 0
    
    for s in s1:
        if s in s2:
            same_count += 1
    
    return same_count