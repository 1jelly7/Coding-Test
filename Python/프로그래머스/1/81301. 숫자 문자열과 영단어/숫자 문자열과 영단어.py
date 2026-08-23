def solution(s):
    number_words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    digits = []
    current_word = []
    
    for ch in s:
        if ch.isdigit():
            digits.append(ch)
            continue
        
        current_word.append(ch)
        
        candidate_word = "".join(current_word)
        if candidate_word in number_words:
            digits.append(number_words[candidate_word])
            current_word.clear()
    
    return int("".join(digits))
    
    # for k, v in number_words.items():
    #     s = s.replace(k, v)
    
    return int(s)