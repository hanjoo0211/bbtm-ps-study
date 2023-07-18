s, d = map(int, input().split())
if (s+d) % 2 == 0 and s >= d:
    print((s+d)//2, (s-d)//2)
else:
    print(-1)