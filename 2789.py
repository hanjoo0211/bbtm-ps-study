cambridge = list("CAMBRIDGE")
word = input()
result = ''
for w in word:
    if w not in cambridge:
        result += w
print(result)
