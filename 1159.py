n = int(input())
players = {}
for _ in range(n):
    p = input()[0]
    if players.get(p):
        players[p] += 1
    else:
        players[p] = 1

lineup = []
for a in players:
    if players[a] >= 5:
        lineup.append(a)
if lineup:
    lineup.sort()
    for l in lineup:
        print(l, end= '')
else:
    print("PREDAJA")