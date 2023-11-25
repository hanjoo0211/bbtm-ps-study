n = int(input())
count = 0
for _ in range(n):
    word = list(input())
    stack = []

    while word:
        w = word.pop()
        if not stack:
            stack.append(w)
        else:
            if w == stack[-1]:
                stack.pop()
            else:
                stack.append(w)
    if not stack:
        count += 1
print(count)
