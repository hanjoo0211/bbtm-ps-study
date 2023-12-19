n = int(input())
a, b = 0, 0
for _ in range(n):
    ai, bi = map(int, input().split())
    if ai > bi:
        a += 1
    elif bi > ai:
        b += 1
print(a, b)
