k = int(input())
fibo = [0, 1]
for _ in range(k-1):
    f = fibo[-1] + fibo[-2]
    fibo.append(f)
print(fibo[-2], fibo[-1])