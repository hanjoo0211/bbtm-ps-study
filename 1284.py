while n := input():
    if n == '0':
        break
    length = 1
    for s in n:
        if s == '1':
            length += 3
        elif s == '0':
            length += 5
        else:
            length += 4
    print(length)