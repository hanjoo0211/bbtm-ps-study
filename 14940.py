from collections import deque

n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "2":
            start = (i, j, 0)
            distance[i][j] = 0
        if board[i][j] == "0":
            distance[i][j] = 0

q = deque([start])
while q:
    x, y, count = q.popleft()
    count += 1
    for dx, dy in d:
        dx = x + dx
        dy = y + dy
        if 0 <= dx < n and 0 <= dy < m and distance[dx][dy] == -1:
            distance[dx][dy] = count
            q.append((dx, dy, count))

for line in distance:
    print(*line)