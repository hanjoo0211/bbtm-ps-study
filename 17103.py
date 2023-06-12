import sys
input = sys.stdin.readline

t = int(input())
ns = [int(input()) for _ in range(t)]
prime = [True for _ in range(max(ns) + 1)]
for i in range(2, max(ns) + 1):
    if prime[i]:
        for j in range(2*i, max(ns) + 1, i):
            prime[j] = False

for n in ns:
    count = 0
    for i in range(2, n//2 + 1):
        if prime[i] and prime[n-i]:
            count += 1
    print(count)