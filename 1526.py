n = int(input())
while set(list(str(n))) - {"4", "7"}:
    n -= 1
print(n)