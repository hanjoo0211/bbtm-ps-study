t = int(input())
for _ in range(t):
    _ = input()
    r, c = map(int, input().split())
    grid = [list(input()) for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'o':
                if 0 < i < r-1 and grid[i-1][j] == 'v' and grid[i+1][j] == '^':
                    count += 1
                if 0 < j < c-1 and grid[i][j-1] == '>' and grid[i][j+1] == '<':
                    count += 1
    print(count)