def solution(s, n):
    # Normalize the shift so it always falls within the alphabet size (26).
    shift = n % 26
    
    result = []
    for ch in s:
        if ch == " ":
            # Spaces are never shifted.
            result.append(" ")
        elif ch.isupper():
            shifted = (ord(ch) - ord("A") + shift) % 26
            result.append(chr(shifted + ord("A")))
        elif ch.islower():
            shifted = (ord(ch) - ord("a") + shift) % 26
            result.append(chr(shifted + ord("a")))
        else:
            result.append(ch)
    
    return "".join(result)