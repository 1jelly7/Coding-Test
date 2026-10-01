def solution(price):
    if price >= 500_000:
        payment_percent = 80
    elif price >= 300_000:
        payment_percent = 90
    elif price >= 100_000:
        payment_percent = 95
    else:
        payment_percent = 100
    
    return price * payment_percent // 100