n = int(input())
attractions = []
for _ in range(n):
    s, e = input().split()
    sh, sm, eh, em = int(s[0:2]), int(s[2:4]), int(e[0:2]), int(e[2:4])
    s = sh * 60 + sm
    e = eh * 60 + em
    s = max(s-10, 600)
    e = min(e+10, 1320)
    attractions.append((s, e))
attractions.sort()

maxTime = 0
time = 600
for s, e in attractions:
    if s >= time:
        maxTime = max(maxTime, s - time)
    time = max(time, e)
maxTime = max(maxTime, 1320 - time)
print(maxTime)