ANT_ATTACKS = (5, 3, 1)

def solution(hp):
    total_ants = 0
    remaining = hp
    
    for attack in ANT_ATTACKS:
        count, remaining = divmod(remaining, attack)
        total_ants += count
    
    return total_ants