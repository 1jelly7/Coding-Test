def solution(numbers):
    sorted_numbers = sorted(numbers)
    
    big_1, big_2 = sorted_numbers[-2:]
    small_1, small_2 = sorted_numbers[:2]
    
    return max(big_1 * big_2, small_1 * small_2)