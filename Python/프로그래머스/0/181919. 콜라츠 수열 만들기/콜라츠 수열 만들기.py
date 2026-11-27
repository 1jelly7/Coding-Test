def solution(n):
    result = [n]
    
    x = n
    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        
        result.append(x)
    
    return result