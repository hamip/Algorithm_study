# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n: int) -> list:
    return [int(i) for i in str(n)[::-1]]
  
