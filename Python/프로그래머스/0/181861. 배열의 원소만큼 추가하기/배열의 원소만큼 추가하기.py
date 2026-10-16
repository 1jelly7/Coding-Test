def solution(arr):
    result = []
    
    for value in arr:
        result += [value] * value
    
    return result