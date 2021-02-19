word = list(input())  #단어를 리스트로 변환

for i in range(97, 123): #a와 z를 아스키 코드 변환
    if chr(i) in word:
        print(word.index(chr(i)), end=' ') #단어에서 해당 알파벳이 있는 위치를 출력, 서식 맞추기
    else:
        print(-1,end=' ')
