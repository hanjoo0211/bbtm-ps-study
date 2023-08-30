n = input()
digit = len(n)
n = int(n)

length = 0
for i in range(1, digit):
    length += i * 9 * (10 ** (i-1))
length += digit * (n - 10 ** (digit-1) + 1)
print(length)