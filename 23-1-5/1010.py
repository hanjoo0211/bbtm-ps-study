def fact(n: int) -> int:
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    bridge = fact(m) // fact(n) // fact(m-n)
    print(bridge)