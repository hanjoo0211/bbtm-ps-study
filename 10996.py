n = int(input())
for i in range(1, n+1):
    s1 = ''
    s2 = ''
    for j in range(n):
        if j % 2 == 0:
            s1 += '*'
            s2 += ' '
        else:
            s1 += ' '
            s2 += '*'
    print(s1)
    print(s2)