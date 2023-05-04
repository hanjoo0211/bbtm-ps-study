n, m = map(int, input().split())
baguni = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j-i+1)//2):
        baguni[i-1+k], baguni[j-1-k] = baguni[j-1-k], baguni[i-1+k]
print(*baguni)