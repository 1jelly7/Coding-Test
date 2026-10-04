def solution(num_list):
    total_mul = 1
    for num in num_list:
        total_mul *= num
    
    total_sum = sum(num_list)
    
    return 1 if total_mul < total_sum ** 2 else 0