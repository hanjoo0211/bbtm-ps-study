while s := input():
    if s == "END":
        break
    s = reversed(s)
    print("".join(s))
