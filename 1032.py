n = int(input())
pattern = list(input())
for _ in range(n-1):
    file = list(input())
    for i in range(len(pattern)):
        if file[i] != pattern[i] and pattern[i] != '?':
            pattern[i] = '?'
answer = ''
for p in pattern:
    answer += p
print(answer)