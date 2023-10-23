bowls = list(input())
height = 0
prev = None
for bowl in bowls:
    if bowl == prev:
        height += 5
    else:
        height += 10
    prev = bowl
print(height)