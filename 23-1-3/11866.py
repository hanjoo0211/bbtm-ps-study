n, k = map(int, input().split())
josephus = []
nums = [i for i in range(1, n+1)]
pointer = 0

while nums:
    pointer += k - 1
    pointer %= len(nums)
    num = nums.pop(pointer)
    josephus.append(num)
print(str(josephus).replace('[', '<').replace(']','>'))