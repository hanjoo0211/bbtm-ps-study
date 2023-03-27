n = int(input())
maxMoney = 0
for _ in range(n):
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[3]:
        money = 50000 + dice[0] * 5000
    elif dice[0] == dice[2] or dice[1] == dice[3]:
        money = 10000 + dice[1] * 1000
    elif dice[0] == dice[1] and dice[2] == dice[3]:
        money = 2000 + dice[0] * 500 + dice[2] * 500
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        money = 1000 + dice[1] * 100
    elif dice[2] == dice[3]:
        money = 1000 + dice[2] * 100
    else:
        money = dice[3] * 100
    maxMoney = max(maxMoney, money)
print(maxMoney)