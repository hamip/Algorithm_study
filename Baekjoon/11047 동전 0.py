n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

coins = coins[::-1]
count = 0

for c in coins:
    if k % c != k:
        count += k // c
        k -= c * (k // c)

print(count)
