from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

def push(n: int):
    queue.append(n)

def pop():
    return queue.popleft() if len(queue) != 0 else -1

def size():
    return len(queue)

def empty():
    return 1 if len(queue) == 0 else 0

def front():
    return queue[0] if len(queue) != 0 else -1

def back():
    return queue[-1] if len(queue) != 0 else -1

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        print(pop())
    elif cmd[0] == "front":
        print(front())
    elif cmd[0] == "back":
        print(back())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
