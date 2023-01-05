n, m = map(int, input().split())
kb = [[n] * n for _ in range(n)]

for i in range(n):
    kb[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    kb[a][b], kb[b][a] = 1, 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            kb[j][k] = min(kb[j][k], kb[j][i] + kb[i][k])

kbnum = [sum(i) for i in kb]
kbu = kbnum.index(min(kbnum))
print(kbu + 1)