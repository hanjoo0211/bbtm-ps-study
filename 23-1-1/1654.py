import sys
input = sys.stdin.readline


k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start, end = 1, max(lans)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for l in lans:
        count += l // mid
    if count < n:
        end = mid - 1
    elif count >= n:
        start = mid + 1

print(end)