from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []
while q:
    q.rotate(-k)
    result.append(q.pop())
print(str(result).replace("[", "<").replace("]", ">"))