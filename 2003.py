n, m = map(int, input().split())
nums = list(map(int, input().split()))
i, j = 0, 0
s = 0
count = 0
while i < n:
    if s <= m:
        if s == m:
            count += 1
        if j == n:
            break
        s += nums[j]
        j += 1
    else:
        s -= nums[i]
        i += 1
print(count)
