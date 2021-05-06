# https://www.acmicpc.net/problem/1259

def isPalindrome(s: str):
    if s == s[::-1]:
        return 'yes'
    else:
        return 'no'

while True:
    s = input()
    if s == '0':
        break
    print(isPalindrome(s))
