def solution(arr, divisor):
    # Keep only the numbers that are divisible by the divisor.
    filtered = [x for x in arr if x % divisor == 0]

    # If no numbers are divisible, return [-1].
    if not filtered:
        return [-1]

    # Sort the remaining numbers in ascending order.
    return sorted(filtered)