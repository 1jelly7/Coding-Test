def solution(num):
    steps = 0
    max_steps = 500
    
    while num != 1:        
        if num & 1:
            num = num * 3 + 1
        else:
            num //= 2
        
        steps += 1
        
        if steps >= max_steps:
            return -1
    
    return steps