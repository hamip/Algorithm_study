from collections import deque

deck = deque([i for i in range(int(input()), 0, -1)])

while len(deck) > 1:
    deck.pop()
    deck.appendleft(deck.pop())

print(deck[0])
