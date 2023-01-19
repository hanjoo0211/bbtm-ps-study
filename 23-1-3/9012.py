import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    stack = []
    string = input()
    for s in string[:-1]:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
        else:
            stack.append('d')
            break
    if stack:
        print('NO')
    else:
        print('YES')