docs = input()
word = input()

newDocs = docs.replace(word, "")
print((len(docs) - len(newDocs)) // len(word))