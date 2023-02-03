from itertools import combinations_with_replacement


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

cwr = list(combinations_with_replacement(nums, m))
for c in cwr:
    r = ''
    for ns in c:
        r += str(ns) + ' '
    print(r[:-1])