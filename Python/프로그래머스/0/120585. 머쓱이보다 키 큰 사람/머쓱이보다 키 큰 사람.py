def solution(array, height):
    return sum(1 for value in array if value > height)