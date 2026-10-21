def solution(str_list, ex):
    return "".join(text for text in str_list if ex not in text)