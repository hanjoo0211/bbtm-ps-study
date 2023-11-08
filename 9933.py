n = int(input())
words = []
for _ in range(n):
    word = input()
    reversed_word = "".join(reversed(word))
    if word == reversed_word or word in words:
        password = word
        break
    words.append(reversed_word)
length = len(password)
middle = password[length // 2]
print(length, middle)
