# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n: int) -> int:
    numbers = set(range(2, n+1)) #2부터 n까지의 숫자들
    for i in range(2, n+1):
        if i in numbers:
            numbers -= set(range(2*i, n+1, i)) # i를 제외하고 i의 배수는 전부 제거
            
    return len(numbers)
  
