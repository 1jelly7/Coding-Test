def solution(arr, divisor):
    if divisor == 0:
        raise ValueError("divisor must a be non-zero integer")
    
    result = [x for x in arr if x % divisor == 0]

    if not result:
        return [-1]

    return sorted(result)