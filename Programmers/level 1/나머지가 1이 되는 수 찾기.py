def solution(n: int) -> int:
    for i in range(2, n):
        if n % i == 1:
            x = i
            break
            
    return x
