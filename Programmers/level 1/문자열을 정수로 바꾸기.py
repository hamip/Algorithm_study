# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s: str) -> int:
    if s[1] == "-":
        return int(s[1:]) * -1
    elif s[1] == "+":
        return int(s[1:])
    else:
        return int(s)
