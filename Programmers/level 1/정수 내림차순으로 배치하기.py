# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n: int) -> int:
    digits = list(str(n))
    digits.sort(reverse=True)
    
    return int("".join(digits))
  
