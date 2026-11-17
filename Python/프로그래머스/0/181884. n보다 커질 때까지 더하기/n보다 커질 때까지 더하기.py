def solution(numbers, n):
    total = 0
    
    for value in numbers:
        if total > n:
            break
        
        total += value
    
    return total