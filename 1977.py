m, n = int(input()), int(input())
a = int((m - 1) ** (1/2)) + 1
b = int(n ** (1/2))
if b < a:
    print(-1)
else:
    squares = [i ** 2 for i in range(a, b+1)]
    print(sum(squares))
    print(squares[0])