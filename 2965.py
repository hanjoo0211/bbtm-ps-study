a, b, c = map(int, input().split())
count = 0
while b - a > 1 or c - b > 1:
    if b - a > c - b:
        b, c = b-1, b
    else:
        a, b = b, b+1
    count += 1
print(count)