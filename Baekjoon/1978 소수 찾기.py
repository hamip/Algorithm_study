def isPrime(n: int) -> int:
    count = 0
    for i in range(2, n+1): # 2부터 n의 제곱근까지 약수
        if n % i == 0:
            count += 1
    
    if count == 1:
        return True
    else:
        return False
    
n = int(input())
counter = 0
num = list(map(int, input().split()))
for x in num:
    if isPrime(x):
        counter += 1

print(counter)
