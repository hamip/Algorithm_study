n, k = map(int, input().split())
num = [i for i in range(1, n+1)]
popped = []
i = 0

while num:
    i += k
    if i > len(num):
        i %= len(num)
        if i == 0:
            i += len(num)
    i -= 1
    popped.append(str(num.pop(i)))

print("<" + ", ".join(popped) + ">")
