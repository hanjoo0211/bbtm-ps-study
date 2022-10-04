from queue import Queue
from itertools import combinations
import copy
import time; start = time.time()


def virus(N: int, M: int, vMap: list):
    virusQueue = Queue()
    for i, line in enumerate(vMap):
            for j, square in enumerate(line):
                if square == '2':
                    virusQueue.put((i, j))

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))             
    while not virusQueue.empty():
        i, j = virusQueue.get()
        for dx, dy in direction:
            di = i + dx
            dj = j + dy
            if 0 <= di < N and 0 <= dj < M and vMap[di][dj] == '0':
                virusQueue.put((di, dj))
                vMap[di][dj] = '2'

    zeroCount = 0
    for line in vMap:
        for square in line:
            if square == '0':
                zeroCount += 1
    
    return zeroCount


n, m = map(int, input().split())
vMap = []
for i in range(n):
    vMap.append(input().split())

zeroSquares = []
for i, line in enumerate(vMap):
        for j, square in enumerate(line):
            if square == '0':
                zeroSquares.append((i, j))

threeWalls = combinations(zeroSquares, 3)
maxZeroSquare = 0
for t in threeWalls:
    newMap = copy.deepcopy(vMap)
    for wall in t:
        newMap[wall[0]][wall[1]] = '1'
    zeroSquare = virus(n, m, newMap)
    maxZeroSquare = max(maxZeroSquare, zeroSquare)

print(maxZeroSquare)
print(time.time() - start)