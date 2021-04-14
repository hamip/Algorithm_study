# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s:str) -> bool:
    if len(s) == 4 or len(s) == 6:
        return True if s.isdigit() else False
    else:
        return False
      
