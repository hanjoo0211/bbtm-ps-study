n = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

total = 0
min_price = 1000000000
for i in range(n-1):
    min_price = min(min_price, oils[i])
    total += min_price * roads[i]
print(total)