n, m = map(int, input().split())
campus = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            di, dj = i, j
            break

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count = 0
stack = [(di, dj)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[di][dj] = True
while stack:
    x, y = stack.pop()
    if campus[x][y] == "P":
        count += 1
    for dx, dy in d:
        dx = x + dx
        dy = y + dy
        if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and campus[dx][dy] != "X":
            visited[dx][dy] = True
            stack.append((dx, dy))
print(count) if count > 0 else print("TT")
