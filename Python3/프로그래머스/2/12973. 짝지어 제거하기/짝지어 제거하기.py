def solution(s):
    # Use a stack to simulate removing adjacent equal characters.
    stack = []
    
    for ch in s:
        # If the top of the stack is the same as the current character,
        # remove it as a pair.
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    # If the stack is empty, all characters were removed successfully.
    return 1 if not stack else 0