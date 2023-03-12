n = int(input())
for i in range(n):
    if i%2 == 0:
        s = '* ' * n
        print(s[:-1])
    else:
        s = ' *' * n
        print(s)