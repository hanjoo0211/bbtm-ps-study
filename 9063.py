n = int(input())
x, y = map(int, input().split())
maxX, maxY, minX, minY = x, y, x, y
for _ in range(n-1):
    x, y = map(int, input().split())
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    minX = min(minX, x)
    minY = min(minY, y)
area = (maxX - minX) * (maxY- minY)
print(area)