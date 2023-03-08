n = int(input())
for i in range(-n+1, n):
    s = '*' * (n - abs(i))
    print(s)