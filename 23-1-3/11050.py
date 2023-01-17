def fact(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


n, k = map(int, input().split())
print(fact(n) // fact(n-k) // fact(k))