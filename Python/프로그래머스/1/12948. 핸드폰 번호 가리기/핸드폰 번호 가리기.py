def solution(phone_number):
    if not isinstance(phone_number, str) or len(phone_number) < 4:
        raise ValueError("phone_number must be a string of length at least 4")
    
    return '*' * (len(phone_number) - 4) + phone_number[-4:]