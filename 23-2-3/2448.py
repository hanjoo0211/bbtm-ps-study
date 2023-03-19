from math import log2


n = int(input())
k = int(log2(n // 3))
star = ['  *  ', ' * * ', '*****']

for i in range(k):
    newStar = []
    for s in star:
        ns = ' ' * 3 * (2**i) + s + ' ' * 3 * (2**i)
        newStar.append(ns)
    for s in star:
        ns = s + ' ' + s
        newStar.append(ns)
    star = newStar

for s in star:
    print(s)