d = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
w, h = map(int, input().split())
while w > 0 and h > 0:
    board = [input().split() for _ in range(h)]
    island = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == "1":
                island += 1
                board[i][j] = "0"
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in d:
                        dx, dy = x + dx, y + dy
                        if 0 <= dx < h and 0 <= dy < w and board[dx][dy] == "1":
                            board[dx][dy] = "0"
                            stack.append((dx, dy))
    print(island)
    w, h = map(int, input().split())