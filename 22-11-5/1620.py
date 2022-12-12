n, m = map(int, input().split())
pkm = {i+1:input() for i in range(n)}
num = {v:k for k, v in pkm.items()}

for _ in range(m):
    ipt = input()
    if ipt.isdigit():
        print(pkm[int(ipt)])
    else:
        print(num[ipt])