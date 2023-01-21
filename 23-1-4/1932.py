n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

maxSum = [[tri[0][0]]]
for i in range(1, n):
    sums = []
    for j in range(i+1):
        if j == 0:
            sums.append(maxSum[i-1][j] + tri[i][j])
        elif j == i:
            sums.append(maxSum[i-1][j-1] + tri[i][j])
        else:
            sums.append(max(maxSum[i-1][j], maxSum[i-1][j-1]) + tri[i][j])
    maxSum.append(sums)
print(max(maxSum[-1]))