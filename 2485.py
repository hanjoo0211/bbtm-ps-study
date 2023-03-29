import math


n = int(input())
tree = [int(input()) for _ in range(n)]
tree.sort()
dist = []
for i in range(1, len(tree)):
    dist.append(tree[i] - tree[i-1])

gcd = dist[0]
for d in dist:
    gcd = math.gcd(gcd, d)

count = 0
for d in dist:
    count += d//gcd - 1
print(count)