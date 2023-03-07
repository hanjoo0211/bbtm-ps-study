n = int(input())
for i in range(n):
    s = ' ' * (n-i-1) + '*' * (i+1)
    print(s)
for i in range(n-1, 0, -1):
    s = ' ' * (n-i) + '*' * i
    print(s)