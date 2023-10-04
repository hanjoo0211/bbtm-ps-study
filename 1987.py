r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

visited_dict = {}
for i in range(65, 91):
    visited_dict[chr(i)] = False
max_visited = 0


def bt(x: int, y: int, visited: dict, count: int) -> None:
    visited[board[x][y]] = True
    count += 1
    can_move = False
    if x+1 < r and not visited[board[x+1][y]]:
        bt(x+1, y, visited, count)
        can_move = True
    if y+1 < c and not visited[board[x][y+1]]:
        bt(x, y+1, visited, count)
        can_move = True
    if x-1 >= 0 and not visited[board[x-1][y]]:
        bt(x-1, y, visited, count)
        can_move = True
    if y-1 >= 0 and not visited[board[x][y-1]]:
        bt(x, y-1, visited, count)
        can_move = True
    if not can_move:
        global max_visited
        max_visited = max(count, max_visited)
    visited[board[x][y]] = False


bt(0, 0, visited_dict, 0)
print(max_visited)
