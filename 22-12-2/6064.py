import sys, math
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    g = math.gcd(m, n)
    q = n // g
    isValid = False

    for i in range(q):
        num = m * i + x
        if (num - y) % n == 0:
            print(num)
            isValid = True
            break

    if not isValid:
        print(-1)