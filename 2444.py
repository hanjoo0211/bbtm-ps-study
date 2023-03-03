n = int(input())
for i in range(2*n-1):
    s = ' ' * abs(n-i-1)
    s += '*' * (2*(n-abs(n-i-1))-1)
    print(s)