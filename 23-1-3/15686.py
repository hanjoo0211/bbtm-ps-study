from itertools import combinations


n, m = map(int, input().split())
city = [input().split() for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            house.append((i, j))
        elif city[i][j] == '2':
            chicken.append((i, j))

chickenDistance = []
for c in chicken:
    ch = []
    for h in house:
        distance = abs(c[0]-h[0]) + abs(c[1]-h[1])
        ch.append(distance)
    chickenDistance.append(ch)

combi = list(combinations(range(len(chicken)), m))
minChickenDistance = 2 * n * len(house)
for cb in combi:
    cd = 0
    for h in range(len(house)):
        minDistance = 2 * n
        for c in cb:
            minDistance = min(minDistance, chickenDistance[c][h])
        cd += minDistance
    minChickenDistance = min(minChickenDistance, cd)
print(minChickenDistance)