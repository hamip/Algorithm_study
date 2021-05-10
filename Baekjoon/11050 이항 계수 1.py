def factorial(x):
    num = 1
    for i in range(1, x+1):
       num *= i
    return num

def bino_coef(n, k) -> int:
    coef = factorial(n) // (factorial(k) * factorial(n - k))

    return coef

n, k = map(int, input().split())
print(bino_coef(n, k))
