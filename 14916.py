n = int(input())
if n in [1, 3]:
    print(-1)
else:
    five = n // 5
    n %= 5
    if n % 2 != 0:
        five -= 1
        n += 5
    two = n // 2
    print(five + two)