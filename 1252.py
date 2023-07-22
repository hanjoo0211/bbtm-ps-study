a, b = input().split()
a, b = "0b" + a, "0b" + b
a, b = int(a, 2), int(b, 2)
print(bin(a+b)[2:])