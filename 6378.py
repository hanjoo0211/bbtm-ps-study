while n := input():
    if n == "0":
        break
    while int(n) >= 10:
        n = str(sum(list(map(int, list(n)))))
    print(n)
