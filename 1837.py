p, k = map(int, input().split())
for r in range(2, int(p ** (1/2)) + 1):
    if r >= k:
        print("GOOD")
        break
    if p % r == 0:
        print("BAD", r)
        break