n, m, s = int(input()), int(input()), input()
s += s[-1]

count = 0
streak = 0
for i in range(m + 1):
    if s[i] == 'I':
        if streak % 2 == 0:
            streak += 1
        else:
            ioi = (streak + 1) // 2 - n
            if ioi > 0:
                count += ioi
            streak = 1
    else:
        if streak % 2 == 0:
            ioi = streak // 2 - n
            if ioi > 0:
                count += ioi
            streak = 0
        else:
            streak += 1
print(count)