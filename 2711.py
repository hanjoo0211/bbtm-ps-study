t = int(input())
for _ in range(t):
    p, s = input().split()
    p = int(p) - 1
    ns = s[:p] + s[p + 1:]
    print(ns)