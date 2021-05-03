import sys

n = int(sys.stdin.readline())
coord = []
for i in range(n):
    coord.append(list(map(int, sys.stdin.readline().split())))

coord.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(coord[i][0], coord[i][1])
