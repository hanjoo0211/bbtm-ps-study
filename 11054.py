n = int(input())
a = list(map(int, input().split()))

c = [[1, 1] for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            c[i][0] = max(c[i][0], c[j][0] + 1)
        elif a[i] < a[j]:
            c[i][1] = max(c[i][1], c[j][0] + 1, c[j][1] + 1)
print(max(max(b) for b in c))