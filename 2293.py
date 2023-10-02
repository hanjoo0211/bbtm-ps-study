n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
s = [1] + [0 for _ in range(k)]

for c in coins:
    for i in range(c, k+1):
        s[i] += s[i-c]
print(s[k])