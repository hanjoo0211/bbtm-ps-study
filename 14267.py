n, m = map(int, input().split())

boss = list(map(int, input().split()))
junior = [[] for _ in range(n)]
for i in range(1, n):
    junior[boss[i]-1].append(i)

compliment = [0 for _ in range(n)]
for _ in range(m):
    i, w = map(int, input().split())
    compliment[i-1] += w

for i in range(1, n):
    for j in junior[i]:
        compliment[j] += compliment[i]
print(*compliment)