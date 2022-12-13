import sys
input = sys.stdin.readline


m = int(input())
s = 0

for _ in range(m):
    opr = input().split()
    if opr[0] == 'all':
        s = (0b1 << 20) - 1
    elif opr[0] == 'empty':
        s = 0
    else:
        opr[1] = int(opr[1]) - 1
        if opr[0] == 'add':
            s = s | (0b1 << opr[1])
        elif opr[0] == 'remove':
            s = s & ~(0b1 << opr[1])
        elif opr[0] == 'toggle':
            s = s ^ (0b1 << opr[1])
        elif opr[0] == 'check':
            print(1 if s & (1 << opr[1]) > 0 else 0)