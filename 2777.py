from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    f = []
    if n == 1:
        print(1)
        continue
    while n > 1:
        isDivided = False
        for i in range(9, 1, -1):
            if n % i == 0:
                isDivided = True
                f.append(i)
                n //= i
                break
        if not isDivided:
            f.append(n)
            break
    if max(f) > 9:
        print(-1)
    else:
        print(len(f))