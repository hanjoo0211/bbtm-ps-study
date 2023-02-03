from itertools import permutations


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

perm = list(permutations(nums, m))
for p in perm:
    r = ''
    for ns in p:
        r += str(ns) + ' '
    print(r[:-1])