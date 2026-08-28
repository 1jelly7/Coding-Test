def solution(name, yearning, photo):
    total = [0] * len(photo)
    
    for i, img in enumerate(photo):
        for n in img:
            if n in name:
                total[i] += yearning[name.index(n)]
    
    return total