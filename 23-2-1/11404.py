import sys
input = sys.stdin.readline


n, m = int(input()), int(input())
INF = 100000 * n
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

for i in range(1, n+1):
    result = ''
    for j in range(1, n+1):
        if cost[i][j] == INF:
            cost[i][j] = 0
        result += str(cost[i][j]) + ' '
    print(result[:-1])