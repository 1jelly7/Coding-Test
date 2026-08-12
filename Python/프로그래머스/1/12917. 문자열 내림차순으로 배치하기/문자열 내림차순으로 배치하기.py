def solution(s):    
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    
    return "".join(sorted(s, reverse=True))