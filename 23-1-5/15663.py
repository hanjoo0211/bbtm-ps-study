from itertools import permutations


n, m = map(int, input().split())
nums = list(map(int, input().split()))

perm = list(set(list(permutations(nums, m))))
perm.sort()
for p in perm:
    r = ''
    for ns in p:
        r += str(ns) + ' '
    print(r[:-1])