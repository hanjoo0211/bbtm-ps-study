n, b = input().split()
b = int(b)
decimal = 0
digit = 1
for s in reversed(n):
    t = ord(s) - 55
    if t < 10:
        t = int(s)
    decimal += t * digit
    digit *= b
print(decimal)