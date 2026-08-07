def binary_trans(s):
    c = len(''.join(s.split('0')))
    count = len(s) - c
    
    answer = []
    while c > 0:
        answer.append(str(c % 2))
        c //= 2
    
    return ''.join(answer[::-1]), count

def solution(s):
    answer = [0, 0]
    while s != '1':
        s, count = binary_trans(s)
        answer[0] += 1
        answer[1] += count
    
    return answer
        