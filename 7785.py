n = int(input())
company = {}
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        company[name] = True
    else:
        company[name] = False
for name in sorted(company, reverse=True):
    if company[name]:
        print(name)