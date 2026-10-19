def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    return int(max(ab, ba))