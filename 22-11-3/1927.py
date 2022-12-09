import heapq, sys
input = sys.stdin.readline


heap = []
n = int(input())
for _ in range(n):
    calc = int(input())
    if calc == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, calc)