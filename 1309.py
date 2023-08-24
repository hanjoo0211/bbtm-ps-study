n = int(input())
lions = [1, 0]
for _ in range(n):
    e, o = lions
    lions = [e+o, e*2+o]
print(sum(lions) % 9901)