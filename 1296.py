yondu = input()
n = int(input())
maxP = 0
maxTeam = []
for _ in range(n):
    team = input()
    l = yondu.count("L") + team.count("L")
    o = yondu.count("O") + team.count("O")
    v = yondu.count("V") + team.count("V")
    e = yondu.count("E") + team.count("E")
    p = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)) % 100
    if p > maxP:
        maxP = p
        maxTeam = [team]
    elif p == maxP:
        maxTeam.append(team)
maxTeam.sort()
print(maxTeam[0])