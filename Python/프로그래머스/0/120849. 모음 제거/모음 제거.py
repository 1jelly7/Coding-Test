def solution(my_string):
    vowels = ("a", "e", "i", "o", "u")
    
    result = [s for s in my_string if s not in vowels]
    
    return "".join(result)