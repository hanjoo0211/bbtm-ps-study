n = int(input())
for i in range(n-1):
    s = ' ' * i
    s += '*' * (2*n-2*i-1)
    print(s)
for i in range(n-1, -1, -1):
    s = ' ' * i
    s += '*' * (2*n-2*i-1)
    print(s)