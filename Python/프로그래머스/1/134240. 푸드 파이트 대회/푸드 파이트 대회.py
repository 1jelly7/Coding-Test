def solution(food):
    left = []
    
    for calorie in range(1, len(food)):
        count = food[calorie] // 2
        left.extend([str(calorie)] * count)
    
    left_str = "".join(left)
    right_str = left_str[::-1]
    
    return left_str + "0" + right_str