n, m = map(int, input().split())
edges = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    edges[v1][v2] = True
    edges[v2][v1] = True

edgeCount = 0
connectCount = 0
isVisited = [True] + [False for _ in range(n)]
while edgeCount < n:
    notVisited = isVisited.index(False)
    stack = [notVisited]
    while len(stack) > 0:
        curNode = stack.pop()
        edgeCount += 1
        isVisited[curNode] = True
        for i, e in enumerate(edges[curNode]):
            if e and not isVisited[i]:
                stack.append(i)
    connectCount += 1

print(connectCount)