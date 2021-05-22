import sys

t = int(input())

for _ in range(t):
    scores = []

    for _ in range(int(sys.stdin.readline())):
        x, y = map(int, sys.stdin.readline().split())
        scores.append((x, y))

    scores.sort(key=lambda x: x[0])
    top = scores[0][1]
    successful_applicants = 1

    for i in range(1, len(scores)):
        if scores[i][1] < top:
            successful_applicants += 1
            top = scores[i][1]

    print(successful_applicants)
