def solution(arr):
    result = []
    
    for value in arr:
        if value >= 50 and value % 2 == 0:
            result.append(value // 2)
        elif value < 50 and value % 2 != 0:
            result.append(value * 2)
        else:
            result.append(value)
    
    return result