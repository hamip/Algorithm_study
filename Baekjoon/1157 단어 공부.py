word = input().upper()  #전부 대문자로
word_list = list(set(word))  #단어의 중복되는 글자들을 빼고, 리스트로 인덱싱 가능하게
count = []             #개수 세기용 리스트
for i in word_list:    
    count.append(word.count(i))   #특정 글자가 단어 안에 사용된 횟수를 개수 리스트에 추가
        
if count.count(max(count)) > 1:   #가장 많이 사용된 알파벳이 두 개 이상 존재할 경우, ? 출력
    print('?')
else:
    print(word_list[count.index(max(count))])  #가장 많이 사용된 알파벳이 개수 리스트의 어느 인덱스에 위치하는지 확인하고, 단어 리스트에서 추출
