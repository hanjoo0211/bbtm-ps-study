n, k = map(int, input().split())
t = list(map(int, input().split()))

maxTempSum = -100 * n
for i in range(n-k+1):
    tempSum = sum(t[i:i+k])
    maxTempSum = max(maxTempSum, tempSum)
print(maxTempSum)