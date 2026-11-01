general_attack = 5
soldier_attack = 3
worker_attack = 1

def solution(hp):
    remains = hp
    
    general_count = remains // general_attack
    remains %= general_attack
    
    soldier_count = remains // soldier_attack
    remains %= soldier_attack
    
    worker_count = remains // worker_attack
    remains %= worker_attack
    
    return general_count + soldier_count + worker_count