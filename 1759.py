l, c = map(int, input().split())
chars = input().split()
chars.sort()
results = []


def bt(word: str, left: list) -> None:
    if len(word) == l:
        results.append(word)
        return
    for i in range(len(left)):
        new_word = word + left[i]
        new_left = left[i+1:]
        bt(new_word, new_left)


bt("", chars)
vowels = ["a", "e", "i", "o", "u"]
for result in results:
    vs = 0
    for r in result:
        if r in vowels:
            vs += 1
    if 1 <= vs <= l - 2:
        print(result)