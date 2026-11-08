def solution(my_string):
    result = []
    
    for ch in my_string:
        if "0" <= ch <= "9":
            result.append(int(ch))
    
    return sorted(result)