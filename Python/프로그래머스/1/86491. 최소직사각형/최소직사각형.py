def solution(sizes):
    max_width, max_height = 0, 0
    
    for card in sizes:
        width, height = max(card), min(card)
        
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height
    
    return max_width * max_height