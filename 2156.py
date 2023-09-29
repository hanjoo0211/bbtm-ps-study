n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0, 0, 0]
for i in range(n):
    dp = [max(dp), dp[0] + wines[i], dp[1] + wines[i]]
print(max(dp))