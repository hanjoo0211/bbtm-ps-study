count = 0
for i in range(8):
    line = input()
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if line[j] == 'F':
                count += 1
    else:
        for j in range(1, 9, 2):
            if line[j] == 'F':
                count += 1
print(count)