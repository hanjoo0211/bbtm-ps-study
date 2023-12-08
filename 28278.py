import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    c = input()
    if c[0] == "1":
        c, x = c.split()
        stack.append(x)
    elif c[0] == "2":
        print(stack.pop()) if stack else print(-1)
    elif c[0] == "3":
        print(len(stack))
    elif c[0] == "4":
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
