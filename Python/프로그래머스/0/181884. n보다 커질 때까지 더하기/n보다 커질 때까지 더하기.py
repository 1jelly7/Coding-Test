from itertools import accumulate

def solution(numbers, n):
    return next(total for total in accumulate(numbers) if total > n)