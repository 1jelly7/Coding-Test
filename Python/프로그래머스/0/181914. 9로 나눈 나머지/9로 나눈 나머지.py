ZERO_CODE = ord("0")

def solution(number):
    return sum(ord(digit) - ZERO_CODE for digit in number) % 9