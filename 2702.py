t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x, y = min(a, b), max(a, b)
    while True:
        r = y % x
        if r == 0:
            break
        y, x = x, r
    gcd = x
    lcm = a * b // gcd
    print(lcm, gcd)