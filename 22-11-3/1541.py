exp = input().split('-')
newExp = []
for e in exp:
    plus = sum(map(int, e.split('+')))
    newExp.append(plus)

result = 2 * newExp[0] - sum(newExp)
print(result)