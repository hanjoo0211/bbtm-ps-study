n = list(input())
nums = {}
for num in n:
    if num == "9":
        num = "6"
    if nums.get(num):
        nums[num] += 1
    else:
        nums[num] = 1
if nums.get("6"):
    nums["6"] = (nums["6"] + 1) // 2
print(max(nums.values()))