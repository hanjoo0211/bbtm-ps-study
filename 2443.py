n = int(input())
for i in range(n):
    s = ' ' * i
    s += '*' * (2 * (n - i) - 1)
    print(s)