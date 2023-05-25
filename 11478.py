s = input()
n = len(s)
strings = []
for i in range(n):
    for j in range(i, n):
        strings.append(s[i:j+1])
print(len(set(strings)))