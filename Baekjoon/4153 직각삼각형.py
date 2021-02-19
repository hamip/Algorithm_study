while True:
    num = list(map(int, input().split())) #인풋을 리스트에 저장
    if sum(num) == 0:    #리스트의 합이 0이면 루프 종료
        break
    diag = max(num)     
    num.remove(diag)
    if num[0] ** 2 + num[1] ** 2 == diag ** 2:
        print('right')
    else:
        print('wrong')
