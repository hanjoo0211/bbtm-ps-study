from collections import deque


n, k = map(int, input().split())

ways = 0
q = deque([(n, 0)])
minCount = 100001
isVisited = [False for _ in range(100001)]
while q:
    p, c = q.popleft()
    isVisited[p] = True
    if p == k and c <= minCount:
        minCount = c
        ways += 1

    nps = []
    if p > 0:
        nps.append(p-1)
    if p < 100000:
        nps.append(p+1)
    if 2 * p <= 100000:
        nps.append(2*p)

    for np in nps:
        if not isVisited[np] and c < minCount:
            q.append((np, c+1))
print(minCount)
print(ways)