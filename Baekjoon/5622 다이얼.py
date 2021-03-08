numList = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
number = input().lower()
callTime = len(number) * 3
for i in range(len(number)):
    for word in numList:
        if number[i] in word:
            callTime += numList.index(word)

print(callTime)
