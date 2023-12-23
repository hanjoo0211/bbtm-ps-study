t = int(input())
for _ in range(t):
    c, v = map(int, input().split())
    d, r = c // v, c % v
    print(f"You get {d} piece(s) and your dad gets {r} piece(s).")
