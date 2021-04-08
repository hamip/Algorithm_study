# https://www.hackerrank.com/challenges/itertools-permutations/problem

# itertools.permutations() 

from itertools import permutations

s, k = input().split()
s = sorted(list(s))
for i in permutations(s, int(k)):
    print("".join(i))
    
    
