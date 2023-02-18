n = int(input())
nums = map(int, input().split())
v = int(input())

count = 0
for ns in nums:
    if ns == v:
        count += 1

print(count)