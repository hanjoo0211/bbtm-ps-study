n = int(input())
while n != -1:
    div = [1]
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    div.sort()
    if n == sum(div):
        s = str(n) + " = "
        for d in div:
            s += str(d) + " + "
        print(s[:-3])
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())