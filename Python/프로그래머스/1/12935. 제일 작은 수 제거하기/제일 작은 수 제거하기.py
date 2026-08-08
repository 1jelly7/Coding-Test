def solution(arr):
    if len(arr) < 2:
        return [-1]
    
    min_val = min(arr)
    arr.remove(min_val)
    
    return arr