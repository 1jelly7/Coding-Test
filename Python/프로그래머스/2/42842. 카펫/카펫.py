def solution(brown, yellow):    
    # Try every possible height of the inner yellow rectangle.
    for height in range(1, yellow + 1):
        # The width must divide the yellow area exactly.
        if yellow % height:
            continue
            
        width = yellow // height
        
        # The full carpet is 2 cells larger in each dimension.
        carpet_width = width + 2
        carpet_height = height + 2
    
        # Check whether the border area matches the brown count.
        if carpet_width * carpet_height - yellow == brown:
            # The problem requires width to be greater than or equal to height.
            return [carpet_width, carpet_height]