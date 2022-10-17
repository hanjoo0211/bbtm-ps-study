import heapq
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
MAXNUM = 10 * 20000 * 300000

ways = [[] * (V+1) for _ in range(V+1)]
distanceToV = [MAXNUM] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    ways[u].append((v, w))

q = []
heapq.heappush(q, (0, K))
distanceToV[K] = 0

while q:
    distance, now = heapq.heappop(q)
    if distanceToV[now] >= distance:
        for w in ways[now]:
            nowDistance = distance + w[1]
            if nowDistance < distanceToV[w[0]]:
                distanceToV[w[0]] = nowDistance
                heapq.heappush(q, (nowDistance, w[0]))

for i in range(1, V+1):
    if distanceToV[i] == MAXNUM:
        print("INF")
    else:
        print(distanceToV[i])