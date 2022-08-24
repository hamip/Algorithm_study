def solution(price: int, money: int, count: int) -> int:
    for i in range(1, count + 1):
        money -= i * price
        
    if money < 0:
        return abs(money)
    else:
        return 0
