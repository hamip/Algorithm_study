def residentNum(floor, roomNum) -> int:
    # a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
    if floor == 0:
        return roomNum
    residents = [i for i in range(1, roomNum + 1)]
    for i in range(floor):
        for j in range(1, roomNum):
            residents[j] += residents[j - 1]

    return residents[-1]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(residentNum(k, n))
