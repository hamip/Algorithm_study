from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque()

def push(n: int):
    stack.append(n)

def pop():
    return stack.pop() if len(stack) != 0 else -1

def top():
    return stack[-1] if stack else -1

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "top":
        print(top())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
