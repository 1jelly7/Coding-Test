from itertools import combinations

def solution(numbers):    
    sums = {a + b for a, b in combinations(numbers, 2)}
    
    return sorted(sums)