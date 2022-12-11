n = int(input())
graph = [input().split() for _ in range(n)]

isSearchFinished = False
while not isSearchFinished:
    isSearchFinished = True
    for r in range(n):
        for c in range(n):
            if graph[r][c] == '1':
                for g in range(n):
                    if graph[c][g] == '1' and graph[r][g] == '0':
                        graph[r][g] = '1'
                        isSearchFinished = False

for r in graph:
    toPrint = ''
    for g in r:
        toPrint += g + ' '
    print(toPrint[:-1])