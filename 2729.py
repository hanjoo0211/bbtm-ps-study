t = int(input())
for _ in range(t):
    a, b = input().split()
    a, b = '0b' + a, '0b' + b
    c = int(a, 2) + int(b, 2)
    print(format(c, 'b'))