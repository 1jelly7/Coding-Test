def solution(array, commands):    
    result = []
    
    for i, j, k in commands:
        start = i - 1
        end = j
        
        if start < 0 or end > len(array) or start >= end:
            raise ValueError("Each command must define a valid non-empty range")
        
        segment = sorted(array[start:end])
        
        if not 1 <= k <= len(segment):
            raise ValueError("k must be within the selected range")
        
        result.append(segment[k - 1])
    
    return result