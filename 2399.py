n = int(input())
x = list(map(int, input().split()))

s = 0
for i in range(n):
    for j in range(n):
        s += abs(x[i] - x[j])
print(s)