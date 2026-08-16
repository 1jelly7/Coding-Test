def solution(s):    
    if not isinstance(s, str):
        raise ValueError("s must be an string")
    
    last_seen = {}
    result = []
    
    for idx, ch in enumerate(s):
        if ch in last_seen:
            result.append(idx - last_seen[ch])
        else:
            result.append(-1)
        
        last_seen[ch] = idx
    
    return result