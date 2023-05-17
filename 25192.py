n = int(input())
people = []
gomgom = 0
for _ in range(n):
    chat = input()
    if chat == 'ENTER':
        gomgom += len(set(people))
        people = []
    else:
        people.append(chat)
gomgom += len(set(people))
print(gomgom)