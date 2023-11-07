n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

min_height, max_height = 1, 100
for i in range(n):
    for j in range(n):
        min_height = min(area[i][j], min_height)
        max_height = max(area[i][j], max_height)

max_safe_area = 1
for h in range(min_height, max_height):
    is_sunk = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] <= h:
                is_sunk[i][j] = True
    safe_area = 0
    stack = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not is_sunk[i][j]:
                safe_area += 1
                visited[i][j] = True
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    for dx, dy in direction:
                        dx = x + dx
                        dy = y + dy
                        if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy] and not is_sunk[dx][dy]:
                            visited[dx][dy] = True
                            stack.append((dx, dy))
    max_safe_area = max(safe_area, max_safe_area)
print(max_safe_area)