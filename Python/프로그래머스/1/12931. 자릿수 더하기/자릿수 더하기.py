def solution(n):
    digits = str(n)
    
    total = 0
    for d in digits:
        total += int(d)
    
    return total