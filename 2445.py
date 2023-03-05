n = int(input())
for i in range(n):
    s = ''
    s += '*' * (i+1)
    s += ' ' * (n-i-1) * 2
    s += '*' * (i+1)
    print(s)
for i in range(n-1, 0, -1):
    s = ''
    s += '*' * (i)
    s += ' ' * (n-i) * 2
    s += '*' * (i)
    print(s)