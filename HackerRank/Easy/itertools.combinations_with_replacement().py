# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

s, k = map(str, input().split())
s = sorted(list(s))
for i in combinations_with_replacement(s, int(k)):
    print("".join(i))
    
