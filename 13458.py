import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

r = 0
for i in a:
    r += 1 + max(math.ceil((i-b) / c), 0)
print(r)