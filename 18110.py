from decimal import Decimal


def round(num):
    d = num % 1
    if d < Decimal("0.5"):
        return int(num)
    return int(num) + 1


n = int(input())
diff = [int(input()) for _ in range(n)]
diff.sort()
excepted = round(n * Decimal("0.15"))

if n == 0:
    answer = 0
elif n < 4:
    answer = round(sum(diff) / n)
else:
    answer = round(sum(diff[excepted:-excepted]) / (n - 2 * excepted))
print(answer)