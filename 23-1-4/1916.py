import heapq
import sys
input = sys.stdin.readline


n, m = int(input()), int(input())
INF = 100000 * n
city = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    city[a-1].append((b-1, c))

s, e = map(int, input().split())
s, e = s-1, e-1

d = [INF for _ in range(n)]
d[s] = 0
pq = []
heapq.heappush(pq, (0, s))

while pq:
    dist, node = heapq.heappop(pq)
    if node == e:
        break
    for b, c in city[node]:
        if dist + c < d[b]:
            d[b] = dist + c
            heapq.heappush(pq, (dist + c, b))
    
print(d[e])