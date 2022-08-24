def solution(n: int) -> int:
    num = ''
    
    while n != 0:
        n, mod = divmod(n, 3)
        num += str(mod)
    
    return int(num, 3)
