# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers: list) -> int:
  # 0부터 9까지 숫자가 있는 집합 num 생성
  num = set(range(10))
  # num에서 numbers를 집합으로 바꾼 것을 뺄셈, sum()으로 합을 구하기
  return sum(num - set(numbers))
