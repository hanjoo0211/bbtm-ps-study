v = int(input())
s = list(input())
a, b = 0, 0
for sv in s:
    if sv == "A":
        a += 1
    else:
        b += 1
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")
