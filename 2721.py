t = int(input())
for _ in range(t):
    n = int(input())
    w = 0
    for k in range(1, n+1):
        tk = (k+2) * (k+1) // 2
        w += k * tk
    print(w)