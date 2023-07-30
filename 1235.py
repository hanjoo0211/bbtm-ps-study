n = int(input())
students = [input() for _ in range(n)]
length = len(students[0])

for k in range(1, length+1):
    newStudents = [s[-k:] for s in students]
    if len(set(newStudents)) == n:
        print(k)
        break