l = int(input())
string = input()
r, m = 31, 1234567891
h = 0
for i in range(l):
    a = ord(string[i]) - 96
    h += (a * (r**i)) % m
print(h % m)