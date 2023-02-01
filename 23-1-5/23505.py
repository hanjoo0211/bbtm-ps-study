n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

print(x[n-k])