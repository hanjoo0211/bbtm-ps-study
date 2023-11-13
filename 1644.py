n = int(input())
prime = []
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i ** (1/2)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)

answer = 0
i, j, s = 0, 0, 0
while j <= len(prime):
    if s == n:
        answer += 1
        if j == len(prime):
            break
        s += prime[j]
        j += 1
    elif s < n:
        if j == len(prime):
            break
        s += prime[j]
        j += 1
    else:
        s -= prime[i]
        i += 1
print(answer)