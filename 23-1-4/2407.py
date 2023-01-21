def fact(n: int) -> int:
    output = 1
    for i in range(1, n+1):
        output *= i
    return output


n, m = map(int, input().split())
comb = fact(n) // fact(m) // fact(n-m)
print(comb)