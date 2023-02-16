from collections import deque


n, k = map(int, input().split())

q = deque([(n, 0)])
minCount = 100001
isVisited = [False for _ in range(100001)]
while q:
    p, c = q.popleft()
    isVisited[p] = True
    if p == k and c <= minCount:
        minCount = c

    nps = []
    if p > 0:
        nps.append((p-1, c+1))
    if p < 100000:
        nps.append((p+1, c+1))
    if 2 * p <= 100000:
        nps.append((2*p, c))

    for np, nc in nps:
        if not isVisited[np] and c < minCount:
            q.append((np, nc))
print(minCount)