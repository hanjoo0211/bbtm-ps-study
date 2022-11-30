n = int(input())
ways = []

for i in range(n+1):
    if i == 0:
        ways.append(0)
    elif i == 1:
        ways.append(1)
    elif i == 2:
        ways.append(3)
    else:
        ways.append(ways[i-1] + 2 * ways[i-2])

print(ways[n] % 10007)