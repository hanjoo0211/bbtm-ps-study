from collections import deque


m, n, h = map(int, input().split())
box = [[input().split() for _ in range(n)] for _ in range(h)]

queue = deque()
for hh in range(h):
    for r in range(n):
        for c in range(m):
            if box[hh][r][c] == '1':
                queue.append((hh, r, c, 0))

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1 ,0), (0, 0, 1), (0, 0, -1)]
isVisited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
while queue:
    hh, r, c, day = queue.popleft()
    today = day
    for d in direction:
        newHH, newR, newC = hh + d[0], r + d[1], c + d[2]
        if 0 <= newHH < h and 0 <= newR < n and 0 <= newC < m and box[newHH][newR][newC] == '0' and not isVisited[newHH][newR][newC]:
            box[newHH][newR][newC] = '1'
            isVisited[newHH][newR][newC] = True
            queue.append((newHH, newR, newC, day + 1))

rawTomatoExist = False
for b in box:
    for r in b:
        if '0' in r:
            rawTomatoExist = True
            break

if rawTomatoExist:
    print(-1)
else:
    print(day)