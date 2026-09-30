def solution(strArr):
    count_dict = {}
    
    for s in strArr:
        if len(s) not in count_dict:
            count_dict[len(s)] = 1
        else:
            count_dict[len(s)] += 1
    
    return max(count_dict.values())