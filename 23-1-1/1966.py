from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    pCount = [0] * 10
    for p in priority:
        pCount[p] += 1
    
    q = deque(enumerate(priority))
    count = 0
    while len(q) > 0:
        doc = q.popleft()
        if sum(pCount[doc[1]:]) == pCount[doc[1]]:
            count += 1
            pCount[doc[1]] -= 1
            if doc[0] == m:
                print(count)
                break
        else:
            q.append(doc)