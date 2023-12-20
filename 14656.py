n = int(input())
students = list(map(int, input().split()))

count = 0
for i in range(n):
    if students[i] != i + 1:
        count += 1
print(count)
