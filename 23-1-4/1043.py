n, m = map(int, input().split())
t = list(map(int, input().split()))
if t[0] == 0:
    t = []
else:
    t = t[1:]
party = [list(map(int, input().split()[1:])) for _ in range(m)]

trueMen = [False for _ in range(n+1)]
while t:
    tm = t.pop()
    trueMen[tm] = True
    for p in party:
        if tm in p:
            for pm in p:
                if not trueMen[pm]:
                    t.append(pm)
                    trueMen[pm] = True

count = 0
for p in party:
    isPartyLie = True
    for pm in p:
        if trueMen[pm]:
            isPartyLie = False
            break
    if isPartyLie:
        count += 1
print(count)