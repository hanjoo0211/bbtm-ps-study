t = int(input())
ns = [int(input()) for _ in range(t)]
p = []
for n in range(max(ns)):
    if n < 3:
        p.append(1)
    elif n < 5:
        p.append(2)
    else:
        p.append(p[n-1] + p[n-5])

for n in ns:
    print(p[n-1])