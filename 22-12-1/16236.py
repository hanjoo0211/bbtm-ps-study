from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if 9 in space[i]:
        shark = (i, space[i].index(9), 0)
        break

size = 2
ate = 0
movedDistance = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while True:
    q = deque([shark])
    isVisited = [[False for _ in range(n)] for _ in range(n)]
    canEat = []
    canEatDist = n * n
    while q:
        x, y, dist = q.popleft()
        if 1 <= space[x][y] < size and dist <= canEatDist:
            canEat.append((x, y))
            canEatDist = dist
        if dist > canEatDist:
            break
        for d in direction:
            dx = x + d[0]
            dy = y + d[1]
            if 0 <= dx < n and 0 <= dy < n and space[dx][dy] <= size and not isVisited[dx][dy]:
                if canEat:
                    if dist+1 <= canEatDist:
                        q.append((dx, dy, dist+1))
                        isVisited[dx][dy] = True
                else:
                    q.append((dx, dy, dist+1))
                    isVisited[dx][dy] = True
    if canEat:
        canEat.sort()
        movedDistance += canEatDist
        space[shark[0]][shark[1]] = 0
        shark = (canEat[0][0], canEat[0][1], 0)
        space[canEat[0][0]][canEat[0][1]] = 9
        ate += 1
        if size == ate and size < 8:
            size += 1
            ate = 0
    else:
        break
print(movedDistance)