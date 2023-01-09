n = int(input())
nums = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
nums.sort()

for f in find:
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if f == nums[mid]:
            break
        elif f < nums[mid]:
            r = mid-1
        else:
            l = mid+1
    if f == nums[mid]:
        print(1)
    else:
        print(0)