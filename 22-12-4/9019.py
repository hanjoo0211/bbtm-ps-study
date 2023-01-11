from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ''))
    isVisited = [False] * 10000
    while True:
        cur = q.popleft()
        if cur[0] == b:
            print(cur[1])
            break
        else:
            d = cur[0] * 2 % 10000
            s = (cur[0] + 9999) % 10000
            l = cur[0] * 10 % 10000 + cur[0] // 1000
            r = cur[0] // 10 + cur[0] % 10 * 1000
            DSLR = [(d, 'D'), (s, 'S'), (l, 'L'), (r, 'R')]
            for num, char in DSLR:
                if not isVisited[num]:
                    q.append((num, cur[1] + char))
                    isVisited[num] = True
