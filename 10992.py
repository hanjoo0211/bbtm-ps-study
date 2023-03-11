n = int(input())
for i in range(n):
    if i == 0:
        s = ' ' * (n-1) + '*'
    elif i == n-1:
        s = '*' * (2*i+1)
    else:
        s = ' ' * (n-i-1) + '*' + ' ' * (2*i-1) + '*'
    print(s)