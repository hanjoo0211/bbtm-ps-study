import heapq, sys
input = sys.stdin.readline


n = int(input())
heap = []
count = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        if count == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            count -= 1
    else:
        heapq.heappush(heap, (abs(num), num))
        count += 1