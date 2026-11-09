def solution(arr, delete_list):
    for value in delete_list:
        if value in arr:
            arr.remove(value)
    
    return arr