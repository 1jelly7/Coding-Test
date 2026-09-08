def solution(num_list):
    evens = 0
    odds = 0
    
    for num in num_list:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return [evens, odds]