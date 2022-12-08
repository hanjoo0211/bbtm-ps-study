n, m = map(int, input().split())
d = [input() for _ in range(n)]
b = [input() for _ in range(m)]

result = list(set(d) & set(b))
result.sort()
print(len(result))
for r in result:
    print(r)