# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a: int, b: int) -> int:
    answer = 0
    if a == b: return a
    elif a * (-1) == b or b * (-1) == a:
        return 0
    else:
        return sum(range(min(a, b), max(a,b)+1))
      
