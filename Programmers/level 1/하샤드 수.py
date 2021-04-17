# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x: int) -> bool:
    if x % sum([int(d) for d in str(x)]) == 0:
        return True
    else:
        return False
      
