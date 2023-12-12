n = int(input())
nums = list(map(int, input().split()))
nums.reverse()

check = 1
stack = []
while nums:
    if nums[-1] == check:
        nums.pop()
        check += 1
    else:
        stack.append(nums.pop())
    while stack:
        if stack[-1] == check:
            stack.pop()
            check += 1
        else:
            break

print("Nice" if not stack else "Sad")
