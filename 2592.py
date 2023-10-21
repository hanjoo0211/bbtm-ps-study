nums = []
nums_count = {}
for _ in range(10):
    num = int(input())
    nums.append(num)
    if nums_count.get(num):
        nums_count[num] += 1
    else:
        nums_count[num] = 1

mean = sum(nums) // 10
max_count = max(nums_count.values())
for k, v in nums_count.items():
    if v == max_count:
        mode = k
        break

print(mean)
print(mode)