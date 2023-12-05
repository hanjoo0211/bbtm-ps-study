n = int(input())
q = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        q[0] += 1
    elif y > 0:
        if x > 0:
            q[1] += 1
        else:
            q[2] += 1
    else:
        if x > 0:
            q[4] += 1
        else:
            q[3] += 1
for i in range(1, 5):
    print(f"Q{i}: {q[i]}")
print(f"AXIS: {q[0]}")
