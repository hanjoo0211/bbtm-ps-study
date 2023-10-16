n = int(input())
students = [input().split() for _ in range(n)]
sorted_students = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in sorted_students:
    print(s[0])