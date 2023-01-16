r, c, t = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if space[i][0] == -1:
        p = i
        break

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(t):
    nextSpace = [[0 for _ in range(c)] for _ in range(r)]
    nextSpace[p][0], nextSpace[p+1][0] = -1, -1

    for i in range(r):
        for j in range(c):
            if space[i][j] > 0:
                pm = space[i][j]
                for d in direction:
                    di = i + d[0]
                    dj = j + d[1]
                    if 0 <= di < r and 0 <= dj < c and space[di][dj] != -1:
                        nextSpace[di][dj] += space[i][j] // 5
                        pm -= space[i][j] // 5
                nextSpace[i][j] += pm
    
    purifiedSpace = [nextSpace[i].copy() for i in range(r)]
    purifiedSpace[p][1] = 0
    for j in range(2, c):
        purifiedSpace[p][j] = nextSpace[p][j-1]
    for i in range(p):
        purifiedSpace[i][c-1] = nextSpace[i+1][c-1]
    for j in range(c-1):
        purifiedSpace[0][j] = nextSpace[0][j+1]
    for i in range(1, p):
        purifiedSpace[i][0] = nextSpace[i-1][0]
    
    purifiedSpace[p+1][1] = 0
    for j in range(2, c):
        purifiedSpace[p+1][j] = nextSpace[p+1][j-1]
    for i in range(p+2, r):
        purifiedSpace[i][c-1] = nextSpace[i-1][c-1]
    for j in range(c-1):
        purifiedSpace[r-1][j] = nextSpace[r-1][j+1]
    for i in range(p+2, r-1):
        purifiedSpace[i][0] = nextSpace[i+1][0]
    
    space = [purifiedSpace[i].copy() for i in range(r)]

remain = 0
for i in range(r):
    for j in range(c):
        if purifiedSpace[i][j] > 0:
            remain += purifiedSpace[i][j]
print(remain)