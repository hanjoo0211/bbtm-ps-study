n = int(input())
for i in range(n):
    s = ' ' * (n-i-1)
    s += '* ' * (i+1)
    print(s[:-1])