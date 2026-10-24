control_dict = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10,
    }

def solution(n, control):
    for ch in control:
        n += control_dict[ch]
    
    return n