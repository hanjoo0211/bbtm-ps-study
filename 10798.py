string = []
maxlen = 0
for _ in range(5):
    s = input()
    maxlen = max(maxlen, len(s))
    string.append(s)

answer = ''
for i in range(maxlen):
    for j in range(5):
        if len(string[j]) > i:
            answer += string[j][i]
print(answer)