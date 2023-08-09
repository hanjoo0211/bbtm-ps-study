n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sumArr = [[0 for _ in range(m+1)] for _ in range(n+1)]
for a in range(n):
    for b in range(m):
        sumArr[a+1][b+1] = sum(sum(arr[c][:b+1]) for c in range(a+1))
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(sumArr[x][y] - sumArr[x][j-1] - sumArr[i-1][y] + sumArr[i-1][j-1])