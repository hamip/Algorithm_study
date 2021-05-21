equation = input().split("-")
order = []

for n in equation:
    if n.isdigit():
        order.append(int(n))
    else:
        order.append(sum(map(int, n.split("+"))))

print(int(order[0])-sum(order[1:]))
