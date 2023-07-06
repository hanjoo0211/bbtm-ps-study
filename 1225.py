a, b = input().split()
a, b = list(a), list(b)
s = 0
for i in a:
    for j in b:
        s += int(i) * int(j)
print(s)