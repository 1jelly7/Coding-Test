NOT_FOUND = -1

def solution(num, k):
    index = str(num).find(str(k))
    
    return index + 1 if index != NOT_FOUND else NOT_FOUND