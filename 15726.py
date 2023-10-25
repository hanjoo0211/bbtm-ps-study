a, b, c = map(int, input().split())
r1 = a * b // c
r2 = a * c // b
print(max(r1, r2))