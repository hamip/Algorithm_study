# https://www.acmicpc.net/problem/1920

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

common_num = set(nums).intersection(set(targets))
for i in targets:
    if i in common_num:
        print(1)
    else:
        print(0)
