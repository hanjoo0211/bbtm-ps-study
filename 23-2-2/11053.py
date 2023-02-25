n = int(input())
a = list(map(int, input().split()))

c = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            c[i] = max(c[i], c[j]+1)
print(max(c))