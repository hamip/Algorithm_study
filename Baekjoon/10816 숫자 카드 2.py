from collections import Counter

n = int(input())
n_counter = Counter(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

ans = []

for num in m_list:
    if num in n_counter.keys():
        ans.append(n_counter[num])
    else:
        ans.append(0)

print(" ".join(map(str, ans)))
