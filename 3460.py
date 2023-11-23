t = int(input())
for _ in range(t):
    n = int(input())
    b = bin(n)[2:]
    one = []
    for i in range(len(b)):
        if b[len(b) - i - 1] == "1":
            one.append(i)
    print(*one)
