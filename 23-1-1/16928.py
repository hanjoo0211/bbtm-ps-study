from collections import deque


n, m = map(int, input().split())
ladder = [tuple(map(int, input().split())) for _ in range(n)]
snake = [tuple(map(int, input().split())) for _ in range(m)]

q = deque([(1, 0)])
isVisited = [False for _ in range(100)]
while q:
    s, c = q.popleft()
    isVisited[s-1] = True
    if s == 100:
        break
    for i in range(1, 7):
        ns = s + i
        nc = c + 1
        for ls in ladder + snake:
            if ls[0] == ns:
                ns = ls[1]
        if ns > 100:
            break
        if not isVisited[ns-1]:
            q.append((ns, c+1))
print(c)