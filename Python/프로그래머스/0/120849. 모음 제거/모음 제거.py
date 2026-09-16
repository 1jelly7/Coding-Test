def solution(my_string):
    vowels = {"a", "e", "i", "o", "u"}
    
    result = [ch for ch in my_string if ch not in vowels]
    
    return "".join(result)