l = int(input())
s = list(map(int, input().split()))
s.sort()
n = int(input())

for i in range(l):
    if s[i] > n:
        a = s[i-1] if i > 0 else 0
        b = s[i]
        break
    elif s[i] == n:
        a, b = n, n
        break
sec = (n-a) * (b-n) - 1
print(sec if sec >= 0 else 0)