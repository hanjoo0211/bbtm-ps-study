n = int(input()) - 1
a, b = 1, 2
for _ in range(2, n+1):
    a, b = b, (a + b) % 15746
if n <= 2:
    print(n+1)
else:
    print(b)