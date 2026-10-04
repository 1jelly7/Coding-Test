def solution(num_list):
    total = 0
    product = 1
    
    for num in num_list:
        total += num
        product *= num
    
    return 1 if product < total ** 2 else 0