import sys
input = sys.stdin.readline


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
mins, maxs = (0, 0, 0), (0, 0, 0)
for i in range(n):
    a, b, c = nums[i]
    minA = min(mins[0], mins[1]) + a
    minB = min(mins) + b
    minC = min(mins[1], mins[2]) + c
    maxA = max(maxs[0], maxs[1]) + a
    maxB = max(maxs) + b
    maxC = max(maxs[1], maxs[2]) + c
    mins = (minA, minB, minC)
    maxs = (maxA, maxB, maxC)
print(max(maxs), min(mins))