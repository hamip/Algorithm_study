def isVPS(s: str):
    stack = []

    for l in s:
        if l == "(":
            stack.append(l)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()         
    
    return len(stack) == 0

for _ in range(int(input())):
    if isVPS(input()):
        print("YES")
    else:
        print("NO")
