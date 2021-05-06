# https://www.acmicpc.net/problem/15649

from itertools import permutations

n, m = map(int, input().split())
num = [str(i) for i in range(1, n+1)]
for i in permutations(num, m):
    print(" ".join(i))
