n = int(input())
people = {"ChongChong": "Dance"}
for _ in range(n):
    a, b = input().split()
    if people.get(a):
        if not people.get(b):
            people[b] = "Dance"
    if people.get(b):
        if not people.get(a):
            people[a] = "Dance"
print(len(people))