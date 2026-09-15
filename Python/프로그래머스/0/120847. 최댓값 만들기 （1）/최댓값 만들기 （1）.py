from itertools import combinations

def solution(numbers):
    combs = combinations(numbers, 2)
    
    result = 0
    for a, b in combs:
        if a * b > result:
            result = a * b
    
    return result