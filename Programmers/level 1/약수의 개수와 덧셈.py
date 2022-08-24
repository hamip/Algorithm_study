def solution(left: int, right: int) -> int:
    res = 0
    # 모든 수는 약수가 적어도 2개이며 약수는 한 쌍씩 더해진다.
    # 따라서 약수의 개수가 홀수개라는 것은 제곱수. 
    
    for n in range(left, right + 1):
        # 제곱수 판별
        if int(n ** 0.5) ** 2 == n:
            res -= n
        else:
            res += n
            
    return res
