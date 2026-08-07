def solution(A,B):
    A_asc = sorted(A)
    B_dsc = sorted(B, reverse=True)
    
    answer = 0
    for i in range(len(A_asc)):
        answer += A_asc[i] * B_dsc[i]
    
    return answer