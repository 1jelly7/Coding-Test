def solution(n):
    # Use dynamic programming to store Fibonacci values.

    if n == 0:
        return 0

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    # Build the sequence from bottom to top.
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 1234567

    return fib[n]