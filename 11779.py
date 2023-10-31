from heapq import heappush, heappop
INF = 100000 * 1000

n = int(input())
cities = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    s, e, c = map(int, input().split())
    cities[s].append((e, c))
start, end = map(int, input().split())

cost = [[INF, []] for _ in range(n+1)]
cost[start] = [0, [start]]
visited = [False for _ in range(n+1)]
now = start
pq = []

while not visited[end]:
    for node, c in cities[now]:
        if cost[now][0] + c < cost[node][0]:
            cost[node][0] = cost[now][0] + c
            cost[node][1] = cost[now][1] + [node]
            heappush(pq, (cost[node][0], node))
    visited[now] = True
    while visited[now] and pq:
        _, now = heappop(pq)

print(cost[end][0])
print(len(cost[end][1]))
print(*cost[end][1])