def solution(n):
    # Count how many 1s are in the binary representation of n.
    target_ones = bin(n).count('1')
    
    # Start checking numbers greater than n one by one.
    candidate = n + 1
    while True:
        # If the candidate has the same number of 1s,
        # it is the answer
        if bin(candidate).count('1') == target_ones:
            return candidate
        candidate += 1