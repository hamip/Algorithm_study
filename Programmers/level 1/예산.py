# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d: list, budget: int) -> int:
    d.sort()
    payment = 0
    max_departments = 0
    
    if sum(d) == budget:
        return len(d)
    else:
        for i in d:
            payment += i
            if payment > budget:
                break
            max_departments += 1
        
        return max_departments
      
