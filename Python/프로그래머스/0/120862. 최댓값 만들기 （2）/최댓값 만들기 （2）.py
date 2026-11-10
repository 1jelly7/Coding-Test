def solution(numbers):
    sorted_numbers = sorted(numbers)
    
    max_product = sorted_numbers[-1] * sorted_numbers[-2]
    min_product = sorted_numbers[0] * sorted_numbers[1]
    
    return max(max_product, min_product)