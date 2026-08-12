n, m = map(int, input().strip().split(' '))

if n <= 0 or m <= 0:
    raise ValueError("n and m must be positive integers")

row = '*' * n + '\n'

print(row * m)