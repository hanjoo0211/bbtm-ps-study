n = int(input())
nums = list(map(int, input().split()))

asc_num = -1
desc_num = 10
asc_iter = 0
desc_iter = 0
max_iter = 0
for num in nums:
    if num >= asc_num:
        asc_num = num
        asc_iter += 1
    else:
        asc_num = num
        max_iter = max(asc_iter, max_iter)
        asc_iter = 1
    if num <= desc_num:
        desc_num = num
        desc_iter += 1
    else:
        desc_num = num
        max_iter = max(desc_iter, max_iter)
        desc_iter = 1
max_iter = max(asc_iter, desc_iter, max_iter)
print(max_iter)
