a, b = map(int, input().split())
s = (a+b) * (abs(b-a)+1) // 2
print(s)