N = int(input())
time = list(map(int, input().split()))

time.sort()
result = 0
for i in range(N):
    result += time[i] * (N-i)
print(result)