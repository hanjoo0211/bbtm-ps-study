xa, ya, xb, yb, xc, yc = map(int, input().split())
if (ya - yb) * (xb - xc) == (xa - xb) * (yb - yc):
    print(-1.0)
else:
    ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** (1/2)
    bc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** (1/2)
    ca = ((xc - xa) ** 2 + (yc - ya) ** 2) ** (1/2)

    rounds = [2 * (ab + bc), 2 * (bc + ca), 2 * (ca + ab)]
    print(max(rounds) - min(rounds))