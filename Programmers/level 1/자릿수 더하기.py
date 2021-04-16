# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n: int) -> int:
    num = 0
    for digit in str(n):
        num += int(digit)

    return num
  
