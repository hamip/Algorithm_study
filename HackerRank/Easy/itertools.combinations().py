# https://www.hackerrank.com/challenges/itertools-combinations/problem

# itertools.combinations()

from itertools import combinations

s, k = input().split()
s = sorted(list(s))
for l in range(1, int(k) + 1):
    for item in combinations(s, l):
        print("".join(item))
