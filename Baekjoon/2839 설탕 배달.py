n = int(input())
bags = 0

while n > 0:
    if n % 5 == 0:
        bags += 1
        n -= 5
    elif n % 3 == 0:
        bags += 1
        n -= 3
    elif n > 5:
        n -= 5
        bags += 1
    else:
        bags = -1
        break

print(bags)
    
