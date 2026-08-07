def solution(numbers):
    valid_digits = set(range(10))
    present_digits = {number for number in numbers if number in valid_digits}
    
    return sum(valid_digits - present_digits)