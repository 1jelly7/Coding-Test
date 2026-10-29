WINNING_HAND = {
    "2": "0",
    "0": "5",
    "5": "2",
}

def solution(rsp):
    return "".join(WINNING_HAND[hand] for hand in rsp)