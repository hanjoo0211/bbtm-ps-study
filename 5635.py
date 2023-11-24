n = int(input())
students = []
for _ in range(n):
    name, day, month, year = input().split()
    d, m, y = map(int, (day, month, year))
    students.append((y, m, d, name))
students.sort()
print(students[-1][3])
print(students[0][3])
