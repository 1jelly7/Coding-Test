def solution(n, m):
    n, m = (n, m) if n > m else (m, n)
    
    max_num = 1
    for num in range(2, m + 1):
        if n % num == 0 and m % num == 0:
            max_num = num
    
    min_num, num = 0, n
    while True:
        if num % n == 0 and num % m == 0:
            min_num = num
            break
        
        num += max_num
    
    return [max_num, min_num]