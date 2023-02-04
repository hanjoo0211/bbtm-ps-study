nums = [list(map(int, input().split())) for _ in range(9)]
maxNum = 0
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if nums[i][j] > maxNum:
            maxNum = nums[i][j]
            x, y = i, j

print(maxNum)
print(x+1, y+1)