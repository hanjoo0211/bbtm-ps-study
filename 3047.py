nums = list(map(int, input().split()))
nums.sort()
nums_dict = {k: num for k, num in zip(["A", "B", "C"], nums)}

result = []
order = list(input())
for o in order:
    result.append(nums_dict[o])
print(*result)
