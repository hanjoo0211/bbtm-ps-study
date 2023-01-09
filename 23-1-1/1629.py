a, b, c = map(int, input().split())

binB = format(b, 'b')
binRemain = []
for i in range(len(binB)):
    if i == 0:
        binRemain.append(a % c)
    else:
        binRemain.append(binRemain[i-1] ** 2 % c)

remainder = 1
for i in range(len(binB)):
    if binB[i] == '1':
        remainder *= binRemain[len(binB)-1-i]
        remainder %= c

print(remainder)