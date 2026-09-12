def solution(n, k):
    lamb = 12000
    drink = 2000
    
    return lamb * n + drink * (k - n // 10)