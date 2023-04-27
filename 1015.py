n = int(input())
a = map(int, input().split())

b = []
for i, aa in enumerate(a):
    b.append([aa, i])
b.sort()

c = []
for j, bb in enumerate(b):
    bb.append(j)
    c.append(bb)
c.sort(key=lambda x:x[1])

result = ''
for i in range(n):
    result += str(c[i][2]) + ' '
print(result[:-1])