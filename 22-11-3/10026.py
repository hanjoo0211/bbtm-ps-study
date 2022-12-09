from copy import deepcopy


n = int(input())
grid = [list(input()) for _ in range(n)]
syGrid = deepcopy(grid)

result = []
for sy in range(2):
    if sy == 1:
        grid = syGrid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'R':
                    grid[i][j] = 'G'
    count = 0
    stack = []
    isVisited = []
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    allAreaFound = False
    while not allAreaFound:
        allAreaFound = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 'X':
                    color = grid[i][j]
                    stack.append((i, j, color))
                    allAreaFound = False
                    break
            if not allAreaFound:
                break
        while len(stack) > 0:
            r, c, color = stack.pop()
            grid[r][c] = 'X'
            for d in direction:
                x, y = r + d[0], c + d[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y] == color and (x, y) not in isVisited:
                    stack.append((x, y, color))
                    isVisited.append((x, y, color))
        if not allAreaFound:
            count += 1

    result.append(count)

print(result[0], result[1])