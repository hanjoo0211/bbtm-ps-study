from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min_count = -1

q = deque([(0, 0, False, 0)])
visited = [[False for _ in range(m)] for _ in range(n)]
broke_visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
while q:
    x, y, broke, count = q.popleft()
    count += 1
    if x == n - 1 and y == m - 1:
        min_count = count
        break
    for i, j in d:
        dx, dy = x + i, y + j
        if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
            if broke:
                if board[dx][dy] == "0" and not broke_visited[dx][dy]:
                    q.append((dx, dy, True, count))
                    broke_visited[dx][dy] = True
            else:
                if board[dx][dy] == "0":
                    q.append((dx, dy, False, count))
                    visited[dx][dy] = True
                else:
                    q.append((dx, dy, True, count))
                broke_visited[dx][dy] = True
print(min_count)
