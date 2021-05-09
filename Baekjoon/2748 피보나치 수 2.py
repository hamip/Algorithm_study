from collections import defaultdict

dp = defaultdict(int)

def fib(N: int) -> int:
    if N <= 1:
        return N

    if dp[N]:
        return dp[N]

    dp[N] = fib(N - 1) + fib(N - 2)

    return dp[N]

print(fib(int(input())))
