SWAP_TABLE = str.maketrans("AB", "BA")

def solution(myString, pat):
    swapped = myString.translate(SWAP_TABLE)
    
    return int(pat in swapped)