def solution(n):
    bin_num = 3
    bin = []
    
    while n > 0:
        bin.append(n % bin_num)
        n //= bin_num
    
    result = 0
    mul = 1
    for num in bin[::-1]:
        result += num * mul
        mul *= bin_num
    
    return result