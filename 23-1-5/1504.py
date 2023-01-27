import heapq
import sys
input = sys.stdin.readline


n, e = map(int, input().split())
INF = 1000 * n
road = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    road[b].append((a, c))

v1, v2 = map(int, input().split())

def dijk(s: int, e: int) -> int:
    d = [INF for _ in range(n+1)]
    d[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        dist, node = heapq.heappop(pq)
        if node == e:
            break
        for b, c in road[node]:
            if dist + c < d[b]:
                d[b] = dist + c
                heapq.heappush(pq, (dist + c, b))
        
    if d[e] == INF:
        return -1
    else:
        return d[e]

r1 = [dijk(1, v1), dijk(v1, v2), dijk(v2, n)]
r2 = [dijk(1, v2), dijk(v2, v1), dijk(v1, n)]
if -1 in r1:
    if -1 in r2:
        print(-1)
    else:
        print(sum(r2))
else:
    if -1 in r2:
        print(sum(r1))
    else:
        print(min(sum(r1), sum(r2)))