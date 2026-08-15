def solution(s):
    if len(s) not in (4, 6):
        return False
    
    return s.isdigit()