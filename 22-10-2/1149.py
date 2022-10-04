n = int(input())
minR, minG, minB = 0, 0, 0
for i in range(n):
    r, g, b = tuple(map(int, input().split()))

    newMinR = min(minG + r, minB + r)
    newMinG = min(minR + g, minB + g)
    newMinB = min(minR + b, minG + b)

    minR = newMinR
    minG = newMinG
    minB = newMinB

print(min(minR, minG, minB))