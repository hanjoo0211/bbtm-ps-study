n, m = map(int, input().split())
d = {i: i for i in range(n+1)}

for _ in range(m):
    f, a, b = map(int, input().split())
    ra, rb = a, b
    ca, cb = 0, 0
    while d[ra] != ra:
        ra = d[ra]
        ca += 1
    while d[rb] != rb:
        rb = d[rb]
        cb += 1
    if f == 0:
        if ca >= cb:
            d[rb] = ra
        else:
            d[ra] = rb
    else:
        if ra == rb:
            print("YES")
        else:
            print("NO")