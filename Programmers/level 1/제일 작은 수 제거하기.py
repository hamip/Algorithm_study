# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr: list) -> list:
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
        
