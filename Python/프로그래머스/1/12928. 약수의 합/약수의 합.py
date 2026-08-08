def solution(n):
    # Sum all proper divisors of n (numbers from 1 up to n//2 that divide n).
    # Then add n itself to get the sum of all divisors including n.
    return n + sum(i for i in range(1, n // 2 + 1) if n % i == 0)