def solution(sides):
    shortest, middle, longest = sorted(sides)
    
    return 1 if longest < shortest + middle else 2