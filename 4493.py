t = int(input())
for _ in range(t):
    n = int(input())
    c1, c2 = 0, 0
    for _ in range(n):
        p1, p2 = input().split()
        if p1 != p2:
            if p1 == "R":
                if p2 == "P":
                    c2 += 1
                else:
                    c1 += 1
            elif p1 == "P":
                if p2 == "S":
                    c2 += 1
                else:
                    c1 += 1
            else:
                if p2 == "R":
                    c2 += 1
                else:
                    c1 += 1
    if c1 > c2:
        print("Player 1")
    elif c2 > c1:
        print("Player 2")
    else:
        print("TIE")
