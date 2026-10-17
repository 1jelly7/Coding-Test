def solution(num_list):
    previous = num_list[-2]
    last = num_list[-1]
    
    if last > previous:
        value = last - previous
    else:
        value = last * 2
    
    num_list.append(value)
    
    return num_list