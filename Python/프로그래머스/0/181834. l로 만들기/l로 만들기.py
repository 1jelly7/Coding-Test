THRESHOLD = "l"

def solution(myString):
    return "".join(max(ch, THRESHOLD) for ch in myString)