N, r, c = map(int, input().split())

result = 0
for i in range(N):
    n = N - i
    q = 2 ** (n - 1)
    if r < q:
        if c < q:
            f = 0
        else:
            f = 1
            c -= q
    else:
        if c < q:
            f = 2
        else:
            f = 3
            c -= q
        r -= q
            
    result += q ** 2 * f

print(result)