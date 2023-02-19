n, m = map(int, input().split())
s = set([input() for _ in range(n)])

count = 0
for _ in range(m):
    st = input()
    if st in s:
        count += 1

print(count)