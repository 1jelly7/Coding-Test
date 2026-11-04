CLAP_DIGITS = frozenset("369")

def solution(order):        
    return sum(1 for digit in str(order) if digit in CLAP_DIGITS)