def solution(d, budget):
    d.sort()
    
    total = 0
    count = 0
    for num in d:
        total += num
        if total <= budget:
            count += 1
        else:
            break
    
    return count