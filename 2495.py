for _ in range(3):
    c = 0
    maxC = 0
    num = input()
    for i in range(1, 8):
        if num[i] == num[i-1]:
            c += 1
        else:
            c = 0
        maxC = max(maxC, c)
    print(maxC+1)