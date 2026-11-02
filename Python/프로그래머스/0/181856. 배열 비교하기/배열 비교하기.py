def _comparison_key(arr):
    return (len(arr), sum(arr))

def solution(arr1, arr2):
    key1 = _comparison_key(arr1)
    key2 = _comparison_key(arr2)
    
    return (key1 > key2) - (key1 < key2)