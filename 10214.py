t = int(input())
for _ in range(t):
    yonsei, korea = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    else:
        print("Draw")
