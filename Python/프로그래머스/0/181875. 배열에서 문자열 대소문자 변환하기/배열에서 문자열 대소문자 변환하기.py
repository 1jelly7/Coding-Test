def solution(strArr):
    result = []
    
    for idx, string in enumerate(strArr):
        if idx % 2 == 1:
            result.append(string.upper())
        else:
            result.append(string.lower())
    
    return result