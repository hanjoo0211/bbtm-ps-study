t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1dict = {}
    for num in note1:
        note1dict[num] = True
    m = int(input())
    note2 = list(map(int, input().split()))
    for num in note2:
        if num in note1dict:
            print(1)
        else:
            print(0)