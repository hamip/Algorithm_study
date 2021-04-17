# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x: int, n: int) -> list:
    if x > 0:
        return [i for i in range(x, n * x + 1, x)]
    elif x < 0:
        return [i for i in range(x, n * x - 1, x)]
    else:
        return [0] * n
