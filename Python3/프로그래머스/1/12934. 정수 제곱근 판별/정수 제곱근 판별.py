def solution(n):
    root = n ** 0.5
    
    return (root + 1) ** 2 if root.is_integer() else -1