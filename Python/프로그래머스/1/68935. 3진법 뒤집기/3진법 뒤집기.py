def solution(n):
    base = 3
    
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    
    reversed = ''.join(digits)
    
    return int(reversed, base)