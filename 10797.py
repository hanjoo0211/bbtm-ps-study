d = input()
cars = input().split()

count = 0
for c in cars:
    if c == d:
        count += 1
print(count)