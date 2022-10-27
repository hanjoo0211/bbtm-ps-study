from collections import deque


N, M = map(int, input().split())
maze = [input() for _ in range(N)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = deque([(0, 0, 1)])
isVisited = [[False for _ in range(M)] for _ in range(N)]
while queue:
    cur = queue.popleft()
    for d in direction:
        row, col = cur[0] + d[0], cur[1] + d[1]
        if 0 <= row < N and 0 <= col < M and maze[row][col] == '1':
            if row == N - 1 and col == M - 1:
                print(cur[2] + 1)
                queue = deque()
                break
            elif isVisited[row][col] == False:
                queue.append((row, col, cur[2] + 1))
                isVisited[row][col] = True