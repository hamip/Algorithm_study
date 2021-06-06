t = int(input())
cnt = 0

for _ in range(t):
    word = input()
    stack = []

    for l in word:
        # if letter is not continuous 
        if l in stack and  stack[-1] != l:
            break    

        stack.append(l)
        if len(stack) == len(word):
            cnt += 1

print(cnt)
