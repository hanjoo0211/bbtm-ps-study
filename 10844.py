n = int(input())
dp = [1 for _ in range(10)]
dp[0] = 0

for _ in range(n-1):
    nextDP = [0 for _ in range(10)]
    for i in range(10):
        if i > 0:
            nextDP[i-1] += dp[i]
        if i < 9:
            nextDP[i+1] += dp[i]
    dp = nextDP
print(sum(dp) % 1000000000)