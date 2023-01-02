import heapq
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    k = int(input())
    minHeap = []
    maxHeap = []
    isAlreadyPopped = [False for _ in range(k)]
    for i in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(minHeap, (n, i))
            heapq.heappush(maxHeap, (-n, i))
        else:
            if n == -1:
                while minHeap:
                    index = heapq.heappop(minHeap)[1]
                    if isAlreadyPopped[index] == False:
                        isAlreadyPopped[index] = True
                        break
            else:
                while maxHeap:
                    index = heapq.heappop(maxHeap)[1]
                    if isAlreadyPopped[index] == False:
                        isAlreadyPopped[index] = True
                        break

    while minHeap:
        minNum, index = heapq.heappop(minHeap)
        if isAlreadyPopped[index] == False:
            heapq.heappush(minHeap, (minNum, index))
            break

    while maxHeap:
        maxNum, index = heapq.heappop(maxHeap)
        if isAlreadyPopped[index] == False:
            heapq.heappush(maxHeap, (maxNum, index))
            break
    
    if minHeap or maxHeap:
        print(-maxNum, minNum)
    else:
        print('EMPTY')