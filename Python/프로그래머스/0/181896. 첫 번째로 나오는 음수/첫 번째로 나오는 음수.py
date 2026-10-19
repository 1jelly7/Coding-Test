def solution(num_list):
    for idx, value in enumerate(num_list):
        if value < 0:
            return idx
    
    return -1