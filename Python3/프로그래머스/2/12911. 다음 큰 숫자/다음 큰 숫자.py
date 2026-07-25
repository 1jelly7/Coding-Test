def solution(n):
    answer = n + 1
    while True:
        n_bin = format(n, 'b')
        answer_bin = format(answer, 'b')
        
        count_n = len([c for c in n_bin if c == '1'])
        count_answer = len([c for c in answer_bin if c == '1'])
        if count_n == count_answer:
            break
        
        answer += 1
    
    return answer