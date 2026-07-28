from collections import Counter

def solution(k, tangerine):
    # Count how many tangerines exist for each size
    size_counts = Counter(tangerine)
    
    # Sort sizes by frequency in descending order.
    counts = sorted(size_counts.values(), reverse=True)
    
    # Pick the most frequent sizes until we have at least k tangerines.
    answer, picked = 0, 0
    for count in counts:
        picked += count
        answer += 1
        
        # Stop as soon as we can collect at least k tangerines.
        if picked >= k:
            break
    
    return answer