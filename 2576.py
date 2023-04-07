nums = [int(input()) for _ in range(7)]
s = 0
minNum = 100

for num in nums:
    if num % 2 == 1:
        s += num
        minNum = min(minNum, num)
if s == 0:
    print(-1)
else:
    print(s)
    print(minNum)