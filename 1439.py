from collections import deque

s = deque(list(input()))
count = 0
now = s[0]
while s:
    if s[0] == now:
        s.popleft()
    elif s[-1] == now:
        s.pop()
    else:
        now = s[0]
        count += 1
    
print(count)