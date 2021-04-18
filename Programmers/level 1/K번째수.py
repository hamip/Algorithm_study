#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array: list, commands: list) -> list:
    answer = []
    for cmd in commands:
        arr = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(arr[cmd[2]-1])
        
    return answer
