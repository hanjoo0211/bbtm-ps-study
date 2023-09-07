n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

maxNums = table[-1].copy()
maxIndex = [n-1 for _ in range(n)]
for _ in range(n):
    m = max(maxNums)
    i = maxNums.index(m)
    maxIndex[i] -= 1
    maxNums[i] = table[maxIndex[i]][i]
print(m)