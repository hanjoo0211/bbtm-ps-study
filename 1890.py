n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ways = [[-1 for _ in range(n)] for _ in range(n)]
ways[-1][-1] = 1

def way(x: int, y:int) -> int:
    if ways[x][y] > -1:
        return ways[x][y]
    else:
        w = 0
        l = board[x][y]
        if l == 0:
            ways[x][y] = 0
            return 0
        if x+l < n:
            w += way(x+l, y)
        if y+l < n:
            w += way(x, y+l)
        ways[x][y] = w
        return w

print(way(0, 0))