n, p = map(int, input().split())
nums = [n]
while True:
    num = nums[-1] * n % p
    if num in nums:
        break
    else:
        nums.append(num)
print(len(nums) - nums.index(num))