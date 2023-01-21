n, m, r = map(int, input().split())
t = list(map(int, input().split()))
MAXLENGTH = 16
road = [[MAXLENGTH for _ in range(n)] for _ in range(n)]

for i in range(n):
    road[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    road[a-1][b-1] = l
    road[b-1][a-1] = l

for i in range(n):
    for j in range(n):
        for k in range(n):
            if road[j][k] > road[j][i] + road[i][k]:
                road[j][k] = road[j][i] + road[i][k]

maxItem = 0
for r in road:
    item = 0
    for i in range(n):
        if r[i] <= m:
            item += t[i]
    maxItem = max(maxItem, item)
print(maxItem)