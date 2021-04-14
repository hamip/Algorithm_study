# programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr: list, divisor: int) -> list:
    answer = sorted([i for i in arr if i % divisor == 0])
    
    if not answer:
        return [-1]
    else: 
        return answer
      
