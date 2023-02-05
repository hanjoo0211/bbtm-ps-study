import sys
input = sys.stdin.readline


n, m = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
ts = [[sum(t[i][:j+1]) for j in range(n)] for i in range(n)]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    s = 0
    for x in range(x1, x2+1):
        if y1 == 0:
            rs = ts[x][y2]
        else:
            rs = ts[x][y2] - ts[x][y1-1]
        s += rs
    print(s)