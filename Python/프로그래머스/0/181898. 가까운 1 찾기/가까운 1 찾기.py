TARGET = 1
NOT_FOUND = -1

def solution(arr, idx):
    try:
        return arr.index(TARGET, idx)
    except ValueError:
        return NOT_FOUND