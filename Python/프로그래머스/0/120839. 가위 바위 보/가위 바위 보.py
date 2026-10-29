def solution(rsp):    
    result = []
    
    for ch in rsp:
        if ch == "2":
            result.append("0")
        elif ch == "0":
            result.append("5")
        elif ch == "5":
            result.append("2")
    
    return "".join(result)