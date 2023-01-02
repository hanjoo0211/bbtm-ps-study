n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    ground += list(map(int, input().split()))
ground.sort()

minCount = 500 * 500 * 256 * 2
minCountHeight = -1
for h in range(ground[0], ground[-1] + 1):
    hb = b
    count = 0
    for g in ground:
        rg = g - h
        if rg < 0:
            count -= rg
            hb += rg
        elif rg > 0:
            count += 2 * rg
            hb += rg
    if hb >= 0 and count <= minCount:
        minCount = count
        minCountHeight = h

print(minCount, minCountHeight)