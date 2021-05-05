# https://www.acmicpc.net/problem/18870

import sys

n = int(sys.stdin.readline())
coord = list(map(int, sys.stdin.readline().split()))
sorted_coord = sorted(set(coord))
compressed = {}

for i in range(len(sorted_coord)):
    compressed[sorted_coord[i]] = i

print(*[compressed[i] for i in coord])
