def solution(left, right):
    result = 0
    
    for num in range(left, right + 1):
        count = 1
        
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                count += 1
        
        result += -num if count % 2 else num
    
    return result