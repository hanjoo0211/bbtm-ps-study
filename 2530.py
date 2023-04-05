a, b, c = map(int, input().split())
d = int(input())

c += d
m = c // 60
c %= 60
b += m
h = b // 60
b %= 60
a += h
a %= 24

print(a, b, c)