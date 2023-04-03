a = list(map(int, input().split()))
b = list(map(int, input().split()))
lastWin = None
aScore, bScore = 0, 0

for i in range(10):
    if a[i] > b[i]:
        lastWin = 'A'
        aScore += 3
    elif a[i] < b[i]:
        lastWin = 'B'
        bScore += 3
    else:
        aScore += 1
        bScore += 1

print(aScore, bScore)
if aScore > bScore:
    print('A')
elif aScore < bScore:
    print('B')
elif lastWin:
    print(lastWin)
else:
    print('D')