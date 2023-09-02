n = int(input())
f0 = 0
f1 = 1
for nn in range(n):
    f = f1
    f1 += f0
    if nn > 0:
        f0 = f
print(f1)