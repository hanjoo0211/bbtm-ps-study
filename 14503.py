n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [input().split() for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서

count = 0
while True:
    if room[r][c] == "0":
        room[r][c] = "-1" # 청소된 상태
        count += 1
    is_movable = False
    for _ in range(4):
        d = (d - 1) % 4 # 반시계 방향
        dx, dy = direction[d]
        x, y = r + dx, c + dy
        if room[x][y] == "0":
            r, c = x, y
            is_movable = True
            break
    if not is_movable:
        dx, dy = direction[d]
        x, y = r - dx, c - dy
        if room[x][y] == "1":
            break
        r, c = x, y
print(count)