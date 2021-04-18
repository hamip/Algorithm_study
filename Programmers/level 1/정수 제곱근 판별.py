# programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n: int) -> int:
    if int(math.sqrt(n)) == math.sqrt(n):
        return (math.sqrt(n) + 1) ** 2
    else:
        return -1
