e, s, m = map(int, input().split())
e, s, m = e % 15, s % 28, m % 19
for i in range(1, 15 * 28 * 19 + 1):
    if i % 15 == e and i % 28 == s and i % 19 == m:
        print(i)
        break