def solution(k, score):
    top_k = []
    result = []
    
    for num in score:
        if len(top_k) < k:
            top_k.append(num)
        elif num > top_k[0]:
            top_k[0] = num
        
        top_k.sort()
        
        result.append(top_k[0])
    
    return result