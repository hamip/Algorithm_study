# https://www.acmicpc.net/problem/2108

from collections import Counter
import sys

def mode(n: list) -> int:
    c = Counter(n).most_common()
    if len(c) > 1:
        if c[0][1] == c[1][1]:
            return c[1][0]
        else:
            return c[0][0]
    else:
        return c[0][0]
        
n = int(input())

num = [int(sys.stdin.readline()) for i in range(n)]
num.sort()

print(round(sum(num)/len(num)))
print(num[len(num)//2])
print(mode(num))
print(max(num) - min(num))
