t = int(input())
size = []

for _ in range(t):
    x, y = map(int, input().split())
    size.append((x, y))

ranks = [1 for _ in range(t)]

for i in range(len(size)):
    for j in range(len(size)):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            ranks[i] += 1

print(*ranks)
