from math import prod

def solution(box, n):
    return prod(side // n for side in box)