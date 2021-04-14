# programmers.co.kr/learn/courses/30/lessons/12917

def solution(s: str) -> str:
    res = sorted(s, reverse=True)
    
    return "".join(res)
  
