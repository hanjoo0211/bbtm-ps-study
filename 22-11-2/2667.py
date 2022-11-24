n = int(input())
house = [list(input()) for _ in range(n)]

danji = []
stack = []
isVisited = []
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
allDanjiFound = False
while not allDanjiFound:
    allDanjiFound = True
    for i in range(n):
        if '1' in house[i]:
            stack.append((i, house[i].index('1')))
            allDanjiFound = False
            break
    count = 0
    while len(stack) > 0:
        r, c = stack.pop()
        count += 1
        house[r][c] = '0'
        for d in direction:
            x, y = r + d[0], c + d[1]
            if 0 <= x < n and 0 <= y < n and house[x][y] == '1' and (x, y) not in isVisited:
                stack.append((x, y))
                isVisited.append((x, y))
    danji.append(count)

result = danji[:-1]
result.sort()
print(len(result))
for i in result:
    print(i)