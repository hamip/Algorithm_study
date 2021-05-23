n = int(input())
num = 0

for i in range(1, n+1):
    digits = list(map(int, str(i)))
    if sum(digits) + i == n:
        num = i
        break

print(num) if num != 0 else print(0)
