def solution(n: int) -> int:
    x = n - 1

    for i in range(2, n):
        if n % i == 1:
            x = i
            break
            
    return x
