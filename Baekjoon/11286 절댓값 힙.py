import heapq, sys

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x), x))
