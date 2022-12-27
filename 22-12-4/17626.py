n = int(input())
one = [i ** 2 for i in range(1, int(n ** (1/2)) + 1)]

if n in one:
    print(1)
else:
    two = []
    for i in range(len(one)):
        for j in range(i, len(one)):
            two.append(one[i] + one[j])
    if n in two:
        print(2)
    else:
        three = []
        for i in two:
            for j in one:
                three.append(i + j)
        if n in three:
            print(3)
        else:
            print(4)