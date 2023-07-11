n, a, b = map(int, input().split())
n, a, b = n-1, a-1, b-1
when = 0
while a != b:
    n, a, b = n//2, a//2, b//2
    when += 1
print(when)