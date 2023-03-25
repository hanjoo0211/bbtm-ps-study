people = 0
maxPeople = 0
for _ in range(10):
    bye, hi = map(int, input().split())
    people -= bye
    people += hi
    maxPeople = max(maxPeople, people)
print(maxPeople)