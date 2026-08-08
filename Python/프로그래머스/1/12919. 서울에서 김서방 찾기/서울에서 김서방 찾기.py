def solution(seoul):
    try:
        idx = seoul.index('Kim')
    except ValueError:
        return '김서방을 찾을 수 없습니다'
    
    return f"김서방은 {idx}에 있다"