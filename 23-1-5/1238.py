import sys
input = sys.stdin.readline
import heapq


n, m, x = map(int, input().split())
INF = 100 * n
road = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    road[s].append((e, t))


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
        
    return d[e]


time = [dijk(i, x) + dijk(x, i) for i in range(1, n+1)]
print(max(time))