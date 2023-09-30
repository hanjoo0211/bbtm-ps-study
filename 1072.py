import math

x, y = map(int, input().split())
z = y * 100 // x

if z < 99:
    r = math.ceil(((z+1) * x - 100 * y) / (100 -(z+1)))
else:
    r = -1
print(r)