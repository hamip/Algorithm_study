n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)
l = 1
for i in range(len(ropes)):
    ropes[i] *= l
    l += 1

print(max(ropes))
