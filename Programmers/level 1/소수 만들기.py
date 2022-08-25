from itertools import combinations

def solution(nums: list) -> int:
    cnt = 0
    l = combinations(nums, 3)
    
    for item in l:
        div = True
        
        for i in range(2, int(sum(item) / 2)):
            if sum(item) % i == 0:
                div = False
                break
        else:
            cnt += 1
            
    return cnt
