def solution(num_list):
    odd_sum = 0
    even_sum = 0
    
    for num in num_list:
        if num % 2 == 0:
            even_sum = even_sum * 10 + num
        else:
            odd_sum = odd_sum * 10 + num
    
    return odd_sum + even_sum