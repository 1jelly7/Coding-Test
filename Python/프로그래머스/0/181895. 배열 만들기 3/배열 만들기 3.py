from itertools import chain

def _slice_closed(arr, start, end):
    return list(arr[start : end + 1])

def solution(arr, intervals):    
    return list(chain.from_iterable(_slice_closed(arr, a, b) for a, b in intervals))