n = int(input())
nums = list(map(int, input().split()))

maxNum = nums[0]
curMaxNum = 0
for i in range(n):
    curMaxNum += nums[i]
    maxNum = max(curMaxNum, maxNum)
    if curMaxNum < 0:
        curMaxNum = 0
print(maxNum)