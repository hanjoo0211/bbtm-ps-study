n = list(map(int, input().split()))


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


minMul = 100 ** 5
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            lcm = n[i] * n[j] // gcd(n[i], n[j])
            lcm = lcm * n[k] // gcd(lcm, n[k])
            minMul = min(lcm, minMul)
print(minMul)