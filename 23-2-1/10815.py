import sys
input = sys.stdin.readline


n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cardDict = {}
for c in card:
    cardDict[c] = 1

for num in nums:
    if num in cardDict:
        print(cardDict[num], end=' ')
    else:
        print(0, end=' ')