def solution(k, tangerine):
    size_set = set(tangerine)
    count_dict = {}
    for size in size_set:
        count_dict[size] = 0
        
    for size in tangerine:
        count_dict[size] += 1
    
    count_list = sorted(count_dict.values(), reverse=True)
    
    """sorted_list = sorted(tangerine)
    
    count_list = []
    start, current_size = 0, sorted_list[0]
    for end in range(1, len(sorted_list)):
        if current_size != sorted_list[end]:
            count_list.append(end - start)
            start = end
            current_size = sorted_list[end]
    count_list.append(end - start + 1)
    count_list.sort(reverse=True)"""
    
    count_sum = 0
    for i, count in enumerate(count_list, start=1):
        count_sum += count
        if count_sum >= k:
            return i
    