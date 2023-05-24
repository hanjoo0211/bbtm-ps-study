n = int(input())
dot = 2
for _ in range(1, n+1):
    dot = dot * 2 - 1
print(dot ** 2)