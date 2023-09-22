s = int(input())
count = 0
i = 1
while s > 0:
    s -= i
    count += 1
    i += 1
if s == 0:
    print(count)
else:
    print(count - 1)