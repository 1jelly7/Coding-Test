keys = ("3", "6", "9")

def solution(order):
    order_text= str(order)
    
    count = 0
    for digit in order_text:
        if digit in keys:
            count += 1
    
    return count