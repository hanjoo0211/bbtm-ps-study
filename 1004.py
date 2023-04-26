T = int(input())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        in1 = True if (cx-x1) ** 2 + (cy-y1) ** 2 < r ** 2 else False
        in2 = True if (cx-x2) ** 2 + (cy-y2) ** 2 < r ** 2 else False
        if in1 != in2:
            count += 1
    print(count)