# programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant: list, completion: list):
    counter = Counter(participant+completion)
    # 완주하지 못한 동명이인이 있거나 완주하지 못한 사람이 있으면 두 리스트를 합한 리스트에서 그 이름이 홀수 개이다
    for i, v in counter.items():
        if v % 2 == 1:
            return i
          
