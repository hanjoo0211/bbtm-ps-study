while True:
    rc = input()
    if rc == "R0C0":
        break
    n, m = rc[1:].split("C")
    m = int(m)
    c = []
    while m > 0:
        r = m % 26
        if r == 0:
            r = 26
        c.append(chr(r + 64))
        m = (m - r) // 26
    print("".join(c[::-1]) + n)