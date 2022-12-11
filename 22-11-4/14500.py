n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
tetra = [((0, 0), (1, 0), (2, 0), (3, 0)), ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1)), ((0, 0), (1, 0), (1, 1), (1, 2)),
        ((0, 0), (1, 0), (1, 1), (2, 1)), ((0, 0), (1, 0), (1, 1), (2, 0))]
direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
rollTetra = [tuple((y, x) for x, y in t) for t in tetra]
tetra += rollTetra

for d in direction:
    for r in range(n):
        for c in range(m):
            for tetromino in tetra:
                tSum = 0
                for b in tetromino:
                    x = r + b[0] * d[0]
                    y = c + b[1] * d[1]
                    if 0 <= x < n and 0 <= y < m:
                        tSum += paper[x][y]
                    else:
                        tSum = -1
                        break
                maxSum = max(tSum, maxSum)

print(maxSum)