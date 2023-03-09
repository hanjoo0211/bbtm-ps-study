n = int(input())
for i in range(n):
    s = ' ' * (n-i-1) + '*'
    if i > 0:
        s += ' ' * (2*i-1) + '*'
    print(s)