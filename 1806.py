n, s = map(int, input().split())
nums = list(map(int, input().split()))

minCount = n + 1
i, j = 0, 0
ps = 0
while i < n:
    if ps < s:
        j += 1
        if j == n + 1:
            break
        ps += nums[j-1]
    else:
        if j - i < minCount:
            minCount = j - i
        i += 1
        ps -= nums[i-1]
if minCount == n + 1:
    print(0)
else:
    print(minCount)