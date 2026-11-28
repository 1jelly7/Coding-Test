from itertools import islice

DIFF_TO_COMMAND = {
    1: "w",
    -1: "s",
    10: "d",
    -10: "a",
}

def solution(numLog):    
    return "".join(
        DIFF_TO_COMMAND[current - previous]
        for previous, current in zip(numLog, islice(numLog, 1, None))
    )