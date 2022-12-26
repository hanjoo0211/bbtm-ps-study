n, m = map(int, input().split())
pwdDict = {}
for _ in range(n):
    k, v = input().split()
    pwdDict[k] = v
for _ in range(m):
    k = input()
    print(pwdDict[k])