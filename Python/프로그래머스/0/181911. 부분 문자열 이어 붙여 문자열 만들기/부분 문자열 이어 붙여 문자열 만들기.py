def solution(my_strings, parts):
    result = ""
    
    for index, part in enumerate(parts):
        result += my_strings[index][part[0] : part[1] + 1]
    
    return result