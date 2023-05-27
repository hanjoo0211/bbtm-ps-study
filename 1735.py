def gcd(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x%y
    return x


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a = a1 * b2 + a2 * b1
b = b1 * b2

g = gcd(a, b)
a, b = a//g, b//g

print(a, b)