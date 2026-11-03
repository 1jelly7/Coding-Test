THRESHOLD = 50

def _transform(x):
    is_even = x % 2 == 0
    
    if x >= THRESHOLD and is_even:
        return x // 2
    if x < THRESHOLD and not is_even:
        return x * 2
    return x

def solution(arr):
    return [_transform(x) for x in arr]