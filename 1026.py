n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
s = 0
for i in range(n):
    s += a[i] * b[n-i-1]
print(s)