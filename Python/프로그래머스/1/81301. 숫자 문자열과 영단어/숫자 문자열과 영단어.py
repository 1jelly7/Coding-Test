def solution(s):
    number_words = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    
    for digit, word in enumerate(number_words):
        s = s.replace(word, str(digit))
    
    return int(s)