from collections import deque

n = int(input())

cards = deque(range(1, n+1))
trash = []
while cards:
    card = cards.popleft()
    trash.append(card)
    cards.rotate(-1)
print(*trash)