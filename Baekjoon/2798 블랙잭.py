from itertools import combinations

n, m = map(int, input().split())
card_numbers = sorted(list(map(int, input().split())))
card_combinations = combinations(card_numbers, 3)
appr = []

for item in card_combinations:
    if sum(item) <= m:
        appr.append(sum(item))

print(max(appr))
