import sys

n = int(sys.stdin.readline())
members = []

for _ in range(n):
    members.append(list(sys.stdin.readline().split()))
# sort by age
members = sorted(members, key=lambda x: (int(x[0])))

for i in members:
    print(i[0], i[1])
