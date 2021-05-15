import math

nums = []

m = int(input())
n = int(input())

for i in range(m, n+1):
    if int(math.sqrt(i)) == math.sqrt(i):
        nums.append(i)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
