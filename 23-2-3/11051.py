n, k = map(int, input().split())


def fact(n: int) -> int:
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


c = fact(n) // fact(k) // fact(n-k)
print(c % 10007)