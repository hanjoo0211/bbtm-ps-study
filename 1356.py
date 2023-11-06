n = input()
is_yujin = False
for i in range(1, len(n)):
    a, b = 1, 1
    for j in n[:i]:
        a *= int(j)
    for k in n[i:]:
        b *= int(k)
    if a == b:
        is_yujin = True
        break
if is_yujin:
    print("YES")
else:
    print("NO")