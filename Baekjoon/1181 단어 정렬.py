n = int(input())
coord = list(set([input() for _ in range(n)]))
sorted_coord = sorted(coord, key=lambda x: (len(x), x))

for i in sorted_coord:
    print(i)
