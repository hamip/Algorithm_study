def solution(absolutes: list, signs: list) -> int:
    total = 0
    for i in range(len(absolutes)):
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]
    return total
