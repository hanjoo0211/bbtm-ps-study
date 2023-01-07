n = int(input())
stack = []
nums = [n-i for i in range(n)]
result = []
isPossible = True
for _ in range(n):
    num = int(input())
    while len(nums) > 0:
        if len(stack) == 0:
            p = nums.pop()
            stack.append(p)
            result.append('+')
        else:
            if stack[-1] == num:
                stack.pop()
                result.append('-')
                break
            else:
                p = nums.pop()
                stack.append(p)
                result.append('+')
    if len(nums) == 0:
        p = stack.pop()
        if num != p:
            isPossible = False
        else:
            result.append('-')

if isPossible:
    for r in result:
        print(r)
else:
    print('NO')