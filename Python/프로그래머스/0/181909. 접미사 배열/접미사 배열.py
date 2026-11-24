def solution(my_string):
    return sorted([my_string[start:] for start in range(len(my_string))])