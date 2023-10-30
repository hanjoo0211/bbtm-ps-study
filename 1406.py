from collections import deque

left, right = deque(input()), deque()
m = int(input())
for _ in range(m):
    cmd = input()
    if cmd[0] == "L" and left:
        c = left.pop()
        right.appendleft(c)
    elif cmd[0] == "D" and right:
        c = right.popleft()
        left.append(c)
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[2])
answer = "".join(list(left) + list(right))
print(answer)