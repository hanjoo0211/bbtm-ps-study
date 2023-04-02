d, k = map(int, input().split())
fibo = [1, 1]
for i in range(2, d):
    fibo.append(fibo[i-2]+fibo[i-1])
first, second = fibo[d-3], fibo[d-2]

a = 1
while (k - a * first) % second != 0:
    a += 1
b = (k - a * first) // second
print(a)
print(b)