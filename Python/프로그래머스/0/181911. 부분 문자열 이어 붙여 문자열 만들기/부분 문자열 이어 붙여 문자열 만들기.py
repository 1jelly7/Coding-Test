def solution(my_strings, parts):
    return "".join(
        text[start : end + 1] for text, (start, end) in zip(my_strings, parts)
    )