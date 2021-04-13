# programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = []
    for item in list(combinations(numbers, 2)):
        answer.append(sum(item))
    answer = sorted(list(set(answer)))

    return answer
  
