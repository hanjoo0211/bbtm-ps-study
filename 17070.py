from collections import deque

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]


# 아래에 벽이 없는지 확인하는 함수
def down(t: tuple) -> bool:
    r, c = t
    if r+1 < n and house[r+1][c] == 0:
        return True
    return False


# 오른쪽에 벽이 없는지 확인하는 함수
def right(t: tuple) -> bool:
    r, c = t
    if c+1 < n and house[r][c+1] == 0:
        return True
    return False


# 오른쪽 대각선 아래에 벽이 없는지 확인하는 함수
def rightdown(t: tuple) -> bool:
    r, c = t
    if r+1 < n and c+1 < n and house[r+1][c+1] == 0:
        return True
    return False


q = deque([((0, 0), (0, 1))])
count = 0
while q:
    s, e = q.pop()
    if e == (n-1, n-1):
        count += 1
        continue
    if s[0] == e[0] and s[1]+1 == e[1]:  # 가로
        if right(e):  # 가로 -> 가로
            q.append((e, (e[0], e[1]+1)))
            if down(e) and rightdown(e):  # 가로 -> 대각선
                q.append((e, (e[0]+1, e[1]+1)))
    elif s[0]+1 == e[0] and s[1] == e[1]:  # 세로
        if down(e):  # 세로 -> 세로
            q.append((e, (e[0]+1, e[1])))
            if right(e) and rightdown(e):  # 세로 -> 대각선
                q.append((e, (e[0] + 1, e[1] + 1)))
    else:  # 대각선
        if right(e):  # 대각선 -> 가로
            q.append((e, (e[0], e[1] + 1)))
        if down(e):
            q.append((e, (e[0] + 1, e[1])))
        if right(e) and down(e) and rightdown(e):
            q.append((e, (e[0] + 1, e[1] + 1)))
print(count)