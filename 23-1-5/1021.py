from collections import deque


n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
q1 = deque(list(range(1, n+1)))
q2 = q1.copy()
for ns in nums:
    c1, c2 = 0, 0
    while q1[0] != ns:
        c1 += 1
        q1.rotate(1)
    q1.popleft()
    while q2[0] != ns:
        c2 += 1
        q2.rotate(-1)
    q2.popleft()
    if c1 < c2:
        count += c1
        q2 = q1.copy()
    else:
        count += c2
        q1 = q2.copy()
print(count)