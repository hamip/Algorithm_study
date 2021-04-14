# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr: list):
    answer = []
    for item in arr:
        if answer[-1:] == [item]:
            continue
        answer.append(item)    
        
    return answer
  
