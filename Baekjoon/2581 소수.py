def isPrime(m: int, n: int) -> list:
    numbers = set(range(m, n+1))

    # remove previous prime number multiples
    if m > 2:
        for i in range(2, m):
            numbers -= set(range(i, n+1, i))
    elif m == 1:
        numbers -= {1}

    for i in range(m, n+1):
        if i in numbers:
            numbers -= set(range(2*i, n+1, i))
            
    return list(numbers)

m = int(input())
n = int(input())

if not isPrime(m, n):
    print(-1)
else:
    print(sum(isPrime(m, n)))
    print(min(isPrime(m, n)))
