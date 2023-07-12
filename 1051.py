n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
width = min(n, m)

while width > 1:
    for i in range(n-width+1):
        for j in range(m-width+1):
            if square[i][j] == square[i][j+width-1] == square[i+width-1][j] == square[i+width-1][j+width-1]:
                print(width ** 2)
                width = 0
                break
        if width == 0:
            break
    width -= 1
if width == 1:
    print(width)