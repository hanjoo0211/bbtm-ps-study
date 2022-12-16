import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    wear = {}
    for wt in range(n):
        w, t = input().split()
        if t in wear:
            wear[t] += 1
        else:
            wear[t] = 1
    
    case = 1
    for c in wear.values():
        case *= c + 1
    print(case - 1)