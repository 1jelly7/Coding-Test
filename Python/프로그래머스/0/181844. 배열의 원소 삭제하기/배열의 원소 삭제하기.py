def solution(arr, delete_list):
    delete_set = set(delete_list)
    
    return [value for value in arr if value not in delete_set]