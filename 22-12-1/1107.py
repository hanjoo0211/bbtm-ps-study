n, m = int(input()), int(input())
broken = []
if m > 0:
    broken = list(map(int, input().split()))
unbroken = [i for i in range(10) if i not in broken]

if m == 10:
    lowMax, highMin = 100, 100
elif unbroken == [0]:
    lowMax, highMin = 0, 100
else:
    lowMax, highMin = n, n
    isBroken = True
    while isBroken and lowMax >= 0:
        isBroken = False
        for d in str(lowMax):
            if int(d) in broken:
                isBroken = True
                break
        if isBroken:
            lowMax -= 1

    isBroken = True
    while isBroken:
        isBroken = False
        for d in str(highMin):
            if int(d) in broken:
                isBroken = True
                break
        if isBroken:
            highMin += 1


def push(num: int, dest: int) -> int:
    if num == -1:
        return abs(n - 100)
    count = 0
    count += len(str(num))
    count += abs(num - dest)
    return count

print(min(push(lowMax, n), push(highMin, n), abs(n - 100)))