from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    p = input()
    p = p.replace('RR', '')
    n = int(input())
    arr = input().replace('[', '').replace(']', '').split(',')
    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr))
    arr = deque(arr)
    isError = False
    isReversed = False

    for q in p:
        if q == 'R':
            isReversed = not isReversed
        elif q == 'D':
            if len(arr) == 0:
                isError = True
                break
            elif isReversed:
                arr.pop()
            else:
                arr.popleft()
    if isReversed:
        arr.reverse()
    
    if isError:
        print('error')
    else:
        print(str(arr).replace(' ', '').replace('deque(', '').replace(')', ''))