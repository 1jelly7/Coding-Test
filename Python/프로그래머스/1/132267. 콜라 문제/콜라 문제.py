def solution(a: int, b: int, n: int) -> int:
    total = 0
    empty = n

    while empty >= a:
        received = empty // a * b

        total += received

        remaining = empty % a

        empty = remaining + received

    return total