n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

count = 0
for i in range(n):
    if nums[i] > x // 2 + 1:
        break
    for j in range(i+1, n):
        if nums[i] + nums[j] == x:
            count += 1
print(count)