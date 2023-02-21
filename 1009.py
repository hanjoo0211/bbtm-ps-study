t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = 1
    for _ in range(b):
        c *= a
        c %= 10
    if c == 0:
        c = 10
    print(c)