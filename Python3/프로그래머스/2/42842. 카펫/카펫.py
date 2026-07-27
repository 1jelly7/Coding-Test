def solution(brown, yellow):
    pairs = set()
    
    for height in range(1, yellow + 1):
        if yellow % height == 0:
            width = yellow // height
            if height > width:
                width, height = height, width
            pairs.add((width, height))
    
    answer = None
    for pair in pairs:
        if (pair[0] + pair[1])*2 + 4 == brown:
            answer = [pair[0] + 2, pair[1] + 2]
    
    return answer