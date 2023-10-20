n, k = map(int, input().split())
temps = list(map(int, input().split()))

s = sum(temps[:k])
max_sum = s
for i in range(n-k):
    s -= temps[i]
    s += temps[i+k]
    max_sum = max(s, max_sum)
print(max_sum)