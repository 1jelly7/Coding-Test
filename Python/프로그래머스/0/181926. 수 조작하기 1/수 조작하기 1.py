commands = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10,
    }

def solution(n, control):
    for command in control:
        n += commands[command]
    
    return n