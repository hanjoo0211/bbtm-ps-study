s = input()
for c in s:
    ac = ord(c)
    if 65 <= ac <= 90:
        r = (ac - 65 + 13) % 26 + 65
    elif 97 <= ac <= 122:
        r = (ac - 97 + 13) % 26 + 97
    else:
        r = ac
    print(chr(r), end="")