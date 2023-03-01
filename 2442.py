n = int(input())

for i in range(n):
    s = ''
    s += ' ' * (n-i-1)
    s += '*' * (2*i+1)
    print(s)