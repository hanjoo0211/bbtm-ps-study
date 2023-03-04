k = int(input())

position = []
x, y = 0, 0
maxX, maxY, minX, minY = 0, 0, 0, 0
for i in range(6):
    d, l = map(int, input().split())
    if d == 1:
        x += l
    elif d == 2:
        x -= l
    elif d == 3:
        y -= l
    elif d == 4:
        y += l
    maxX = max(maxX, x)
    minX = min(minX, x)
    maxY = max(maxY, y)
    minY = min(minY, y)
    position.append((x, y))

big = (maxX-minX) * (maxY-minY)
for x, y in position:
    if x not in [maxX, minX] and y not in [maxY, minY]:
        i = position.index((x, y))
        px, py = position[i-1]
        nx, ny = position[(i+1)%6]
        x1, y1 = x - px, y - py
        x2, y2 = x - nx, y - ny
        small = abs((x1+x2) * (y1+y2))
        break
print((big-small) * k)