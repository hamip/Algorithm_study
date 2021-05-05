# https://www.acmicpc.net/problem/11653

n = int(input())
div = 2

while n != 1:
    if n % div == 0:
        print(div)
        n /= div
    else:
        div += 1
