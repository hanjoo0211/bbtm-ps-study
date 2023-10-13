from collections import deque

d = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)]

t = int(input())
for _ in range(t):
    l = int(input())
    kx, ky = tuple(map(int, input().split()))
    tx, ty = tuple(map(int, input().split()))

    q = deque([(kx, ky, 0)])
    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[kx][ky] = True

    while q:
        x, y, c = q.popleft()
        if x == tx and y == ty:
            break
        for dx, dy in d:
            dx = x + dx
            dy = y + dy
            if 0 <= dx < l and 0 <= dy < l and not visited[dx][dy]:
                visited[dx][dy] = True
                q.append((dx, dy, c+1))
    print(c)