from collections import deque


a, b = map(int, input().split())
q = deque([(a, 1)])

isPossible = False
while q:
    n, c = q.popleft()
    if n == b:
        isPossible = True
        break
    elif n < b:
        q.append((n*2, c+1))
        q.append((n*10+1, c+1))
if isPossible:
    print(c)
else:
    print(-1)