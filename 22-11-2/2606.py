n = int(input())
v = int(input())

virus = [0 for _ in range(n+1)]
network = [[] for _ in range(n+1)]
for _ in range(v):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)

virus[1] = 1
stack = network[1].copy()

while len(stack) > 0:
    node = stack.pop()
    virus[node] = 1
    for _ in network[node]:
        if virus[_] == 0:
            stack.append(_)

print(sum(virus) - 1)