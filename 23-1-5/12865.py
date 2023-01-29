n, k = map(int, input().split())
t = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        w = t[i][0]
        v = t[i][1]
        if w > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-w] + v)
print(knapsack[-1][-1])