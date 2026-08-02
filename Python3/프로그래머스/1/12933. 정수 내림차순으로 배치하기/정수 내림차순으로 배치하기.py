def solution(n):
    # Convert the number to a string so each digit can be handled separately.
    digits = list(str(n))

    # Sort the digits in descending order.
    digits.sort(reverse=True)

    # Join the sorted digits back into a string and convert it to an integer.
    return int(''.join(digits))