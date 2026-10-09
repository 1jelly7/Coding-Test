def solution(a, b):
    concatenation = int(f"{a}{b}")
    product = 2 * a * b
    
    return max(concatenation, product)