a, b, c, d, e, f = map(int, input().split())
answer = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            answer = [x, y]
            break
    if answer:
        break
print(*answer)