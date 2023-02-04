n = list(map(int, input().split()))
n.sort()

if n[0] == n[2]:
    print(n[2]*1000 + 10000)
elif n[0] == n[1] or n[1] == n[2]:
    print(n[1]*100 + 1000)
else:
    print(n[2]*100)