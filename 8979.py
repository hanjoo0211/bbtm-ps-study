n, k = map(int, input().split())
countries = []
for _ in range(n):
    country = list(map(int, input().split()))
    countries.append(country)
rank = sorted(countries, key=lambda x: (x[1], x[2], x[3], x[0]==k), reverse=True)
for i in range(n):
    if rank[i][0] == k:
        print(i+1)
        break