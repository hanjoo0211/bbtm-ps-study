a, b = map(int, input().split())
nums = [0]
count = 0
i = 1
while count < b:
    for j in range(i):
        nums.append(i)
        count += 1
    i += 1
print(sum(nums[a:b+1]))