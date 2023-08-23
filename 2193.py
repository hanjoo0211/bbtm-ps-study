n = int(input())
pinary = [[0, 1]]
for i in range(1, n):
    z, o = pinary[-1]
    pinary.append([z+o, z])
print(sum(pinary[-1]))