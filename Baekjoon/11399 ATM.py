n = int(input())
people = sorted(list(map(int, input().split())))
time = 0

for i in range(n):
    time += sum(people[0:i+1])

print(time)
