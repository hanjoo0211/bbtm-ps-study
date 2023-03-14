n = int(input())
p = int(input())
minP = p
if n >= 20:
    minP = min(p*3//4, minP)
if n >= 15:
    minP = min(p-2000, minP)
if n >= 10:
    minP = min(p*9//10, minP)
if n >= 5:
    minP = min(p-500, minP)
print(max(0, minP))