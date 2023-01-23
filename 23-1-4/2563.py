n = int(input())
paper = [[False for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = True
area = 0
for x in paper:
    for y in x:
        if y:
            area += 1
print(area)