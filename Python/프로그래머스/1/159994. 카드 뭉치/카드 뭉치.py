from typing import List

def solution(cards1: List[str], cards2: List[str], goal: List[str]) -> str:    
    for name, value in (("cards1", cards1), ("cards2", cards2), ("goal", goal)):
        if not isinstance(value, list) or not all(isinstance(word, str) for word in value):
            raise TypeError(f"{name} must be a list of strings.")
    
    idx1, idx2 = 0, 0
    
    for word in goal:        
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        else:
            return "No"
    
    return "Yes"