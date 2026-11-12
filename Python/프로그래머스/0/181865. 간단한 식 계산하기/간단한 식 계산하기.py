def solution(binomial):
    left, op, right = binomial.split()
    
    left = int(left)
    right = int(right)
    
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right