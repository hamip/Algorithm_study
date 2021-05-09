num = [int(input()) for _ in range(7)]
total = []

for i in num:
    if i % 2 == 1:
        total.append(i)
        
if not total:
    print(-1)
else:  
    print(sum(total))
    print(min(total))
