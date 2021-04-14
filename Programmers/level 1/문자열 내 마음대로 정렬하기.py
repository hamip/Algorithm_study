# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings: list, n: int) -> list:
    # first sort in lexicographical order, then by nth letter of each item
    answer = sorted(sorted(strings), key=lambda x: x[n])
    
    return answer
  
  
