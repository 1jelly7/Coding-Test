def solution(s):
    result = []
    idx_in_word = 0
    
    for ch in s:
        if ch == " ":
            result.append(ch)
            idx_in_word = 0
        else:
            if idx_in_word % 2 == 0:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
            idx_in_word += 1
    
    return "".join(result)