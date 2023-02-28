n = int(input())
call = list(map(int, input().split()))

yfee = 0
mfee = 0
for c in call:
    yfee += 10 * (c // 30 + 1)
    mfee += 15 * (c // 60 + 1)

if yfee == mfee:
    print('Y M ' + str(yfee))
elif yfee < mfee:
    print('Y ' + str(yfee))
else:
    print('M ' + str(mfee))