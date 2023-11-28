n = int(input())
all_nums = [list(map(int, input().split())) for _ in range(n)]
scores = [0 for _ in range(n)]

for i in range(3):
    nums = [all_nums[j][i] for j in range(n)]
    for j in range(n):
        if nums.count(nums[j]) < 2:
            scores[j] += nums[j]
[print(score) for score in scores]
