# https://www.acmicpc.net/problem/15650

from itertools import combinations

n, m = map(int, input().split())
num = [str(i) for i in range(1, n+1)]
for i in combinations(num, m):
    print(" ".join(i))
