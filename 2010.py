n = int(input())
cpu = 1
for _ in range(n):
    plugs = int(input())
    cpu += plugs - 1
print(cpu)