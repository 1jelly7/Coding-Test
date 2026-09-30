from collections import Counter

def solution(strArr):
    length_counts = Counter(len(value) for value in strArr)
    
    return max(length_counts.values())