commands = {
    1: "w",
    -1: "s",
    10: "d",
    -10: "a",
}

def solution(numLog):
    result = []
    current = numLog[0]
    
    for i in range(1, len(numLog)):
        result.append(commands[numLog[i] - current])
        current = numLog[i]
    
    return "".join(result)