N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.reverse()
count = 0
for c in coins:
    while c <= K:
        K -= c
        count += 1

print(count)