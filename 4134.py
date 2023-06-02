t = int(input())
for _ in range(t):
    n = int(input())
    isPrime = False
    if n < 2:
        isPrime = True
        n = 2
    while not isPrime:
        isPrime = True
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                isPrime = False
                break
        if not isPrime:
            n += 1
    print(n)