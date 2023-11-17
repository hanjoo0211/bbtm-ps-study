n = int(input())
classes = [input().split() for _ in range(n)]
same_class = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(5):
            if i != j and same_class[i][j] == 0:
                if classes[i][k] == classes[j][k]:
                    same_class[i][j] = 1

max_same_class = 0
student = 0
for i in range(n):
    if sum(same_class[i]) > max_same_class:
        max_same_class = sum(same_class[i])
        student = i
print(student + 1)
