r = 1000 - int(input())
count = 0
while r > 0:
    for unit in [500, 100, 50, 10, 5, 1]:
        if r >= unit:
            r -= unit
            break
    count += 1
print(count)