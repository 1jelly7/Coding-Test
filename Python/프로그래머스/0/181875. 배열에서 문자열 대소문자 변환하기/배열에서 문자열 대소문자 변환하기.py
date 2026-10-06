def solution(strArr):
    result = []
    
    for index, text in enumerate(strArr):
        if index % 2 == 1:
            converted_text = text.upper()
        else:
            converted_text = text.lower()
        
        result.append(converted_text)
    
    return result