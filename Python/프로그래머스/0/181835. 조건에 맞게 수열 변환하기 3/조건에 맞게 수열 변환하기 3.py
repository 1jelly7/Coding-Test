def solution(arr, k):    
    if k % 2 == 0:
        return [value + k for value in arr]
    
    return [value * k for value in arr]