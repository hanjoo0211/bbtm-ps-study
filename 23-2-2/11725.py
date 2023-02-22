n = int(input())
parent = [0 for _ in range(n+1)]
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

stack = [1]
isVisited = [False for _ in range(n+1)]
isVisited[1] = True
while stack:
    node = stack.pop()
    for nd in g[node]:
        if not isVisited[nd]:
            parent[nd] = node
            stack.append(nd)
            isVisited[nd] = True

for i in range(2, n+1):
    print(parent[i])