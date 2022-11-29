from collections import deque


m, n = map(int, input().split())
box = [input().split() for _ in range(n)]

queue = deque()
for r in range(n):
    for c in range(m):
        if box[r][c] == '1':
            queue.append((r, c, 0))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
isVisited = [[False for _ in range(m)] for _ in range(n)]
while queue:
    r, c, day = queue.popleft()
    today = day
    for d in direction:
        newR, newC = r + d[0], c + d[1]
        if 0 <= newR < n and 0 <= newC < m and box[newR][newC] == '0' and not isVisited[newR][newC]:
            box[newR][newC] = '1'
            isVisited[newR][newC] = True
            queue.append((newR, newC, day + 1))

rowTomatoExist = False
for b in box:
    if '0' in b:
        rowTomatoExist = True
        break

if rowTomatoExist:
    print(-1)
else:
    print(day)