def solution(cards1, cards2, goal):
    i1, i2, i3 = 0, 0, 0
    
    while True:
        if i3 >= len(goal):
            return "Yes"
        
        if i1 < len(cards1) and goal[i3] == cards1[i1]:
            i1 += 1
            i3 += 1
        elif i2 < len(cards2) and goal[i3] == cards2[i2]:
            i2 += 1
            i3 += 1
        else:
            break
    
    return "No"