t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    np = list(map(int, input().split()))
    mp = list(map(int, input().split()))
    np.sort()
    np.reverse()
    mp.sort()
    mp.reverse()

    while np and mp:
        if np[-1] >= mp[-1]:
            mp.pop()
        else:
            np.pop()
    
    if np:
        print("S")
    else:
        print("B")