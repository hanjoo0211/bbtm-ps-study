nums = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(9-i-1):
        fake = nums[i], nums[i+j+1]
        if sum(nums) - sum(fake) == 100:
            for n in nums:
                if n not in fake:
                    print(n)
            break
