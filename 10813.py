n, m = map(int, input().split())
baguni = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
print(*baguni)