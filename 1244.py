n = int(input())
switches = list(map(bool, map(int, input().split())))
m = int(input())
for _ in range(m):
    gender, switch = map(int, input().split())
    if gender == 1:
        for i in range(switch, n+1, switch):
            switches[i-1] = not switches[i-1]
    else:
        lr = min(switch-1, n-switch)
        switch -= 1
        switches[switch] = not switches[switch]
        for i in range(1, lr+1):
            if switches[switch-i] == switches[switch+i]:
                switches[switch-i] = not switches[switch-i]
                switches[switch+i] = not switches[switch+i]
            else:
                break

for i, s in enumerate(switches):
    if s:
        print(1, end=' ')
    else:
        print(0, end=' ')
    if i % 20 == 19:
        print("")