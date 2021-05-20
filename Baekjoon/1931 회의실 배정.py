n = int(input())
meeting_times = []

for _ in range(n):
    x, y = map(int, input().split())
    meeting_times.append((x, y))

meeting_times.sort(key=lambda x: (x[1], x[0]))

ending_time = meeting_times[0][1]
count = 1

for i in range(1, n):
    if  meeting_times[i][0] >= ending_time:
        count += 1
        ending_time = meeting_times[i][1]

print(count)
