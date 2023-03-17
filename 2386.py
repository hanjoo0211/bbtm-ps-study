while s := input():
    if s == "#":
        break
    else:
        count = 0
        for w in s[2:]:
            if w in [s[0], s[0].upper()]:
                count += 1
        print(s[0], count)