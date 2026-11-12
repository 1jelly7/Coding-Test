def solution(arr, n):
    result = arr.copy()
    
    start_index = 0 if len(arr) % 2 == 1 else 1
    
    for i in range(start_index, len(result), 2):
        result[i] += n
    
    return result