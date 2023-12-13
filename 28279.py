from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    c = input()
    if c[0] == "1":
        c, x = c.split()
        q.appendleft(x)
    elif c[0] == "2":
        c, x = c.split()
        q.append(x)
    elif c[0] == "3":
        print(q.popleft() if q else -1)
    elif c[0] == "4":
        print(q.pop() if q else -1)
    elif c[0] == "5":
        print(len(q))
    elif c[0] == "6":
        print(0 if q else 1)
    elif c[0] == "7":
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
