t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    r = min(A, B)
    b = max(A, B)
    while r > 0:
        a = b
        b = r
        r = a % b
    gcd = b
    lcm = A * B // gcd
    print(lcm)