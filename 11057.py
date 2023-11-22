n = int(input())
nums = [1] * 10
for i in range(n-1):
    new_nums = []
    for j in range(10):
        new_nums.append(sum(nums[j:]))
    nums = new_nums
print(sum(nums) % 10007)
