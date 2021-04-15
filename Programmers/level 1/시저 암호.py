# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s: str, n: int) -> str:
    answer = ''
    for letter in s:
        if letter.isupper():
            answer += chr((ord(letter) - ord('A') + n) % 26 + ord('A'))
        elif letter.islower():
            answer += chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += letter
    
    return answer
