n = int(input())
bows = list(map(int, input().split()))

enemies = 0
max_enemies = 0
prev_bow = 0
for bow in bows:
    if bow > prev_bow:
        max_enemies = max(enemies, max_enemies)
        enemies = 0
        prev_bow = bow
    else:
        enemies += 1
max_enemies = max(enemies, max_enemies)
print(max_enemies)