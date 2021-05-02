# https://www.acmicpc.net/problem/1427

n = input()
digits = sorted([i for i in n], reverse=True)
print("".join(digits))
