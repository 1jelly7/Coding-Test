def solution(arr1, arr2):        
    if not arr1 or not arr2:
        raise ValueError("Both matrices must be non-empty")
    
    if len(arr1) != len(arr2) or \
    any(len(r1) != len(r2) for r1, r2 in zip(arr1, arr2)):
        raise ValueError("Matrices must have the same dimensions")
    
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]