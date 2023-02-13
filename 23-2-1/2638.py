from collections import deque


n, m = map(int, input().split())
s = [input().split() for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cheese = []
for i in range(n):
    for j in range(m):
        if s[i][j] == '1':
            cheese.append((i, j))

count = 0
while cheese:
    oq = deque([(0, 0)])
    s[0][0] = '2'
    while oq:
        ox, oy = oq.popleft()
        for d in direction:
            nx = ox + d[0]
            ny = oy + d[1]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == '0':
                oq.append((nx, ny))
                s[nx][ny] = '2'
    
    change = []
    for i, j in cheese:
        oc = 0
        for d in direction:
            x = i + d[0]
            y = j + d[1]
            if s[x][y] == '2':
                oc += 1
        if oc >= 2:
            change.append((i, j))
    
    for i, j in change:
        s[i][j] = '2'
        cheese.remove((i, j))

    for i in range(n):
        for j in range(m):
            if s[i][j] == '2':
                s[i][j] = '0'

    count += 1

print(count)