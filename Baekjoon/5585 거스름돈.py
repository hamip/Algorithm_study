n = int(input())
change = 1000 - n

coins = [500, 100, 50, 10, 5, 1]
count = 0

for c in coins:
    if change // c >= 1:
        count += change // c
        change %= c

print(count)
