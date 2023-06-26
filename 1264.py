while True:
    string = input()
    count = 0
    if string == '#':
        break
    for s in string:
        if s in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            count += 1
    print(count)
    