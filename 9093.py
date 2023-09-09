t = int(input())
for _ in range(t):
    words = input().split()
    for i in range(len(words)):
        words[i] = ''.join(reversed(words[i]))
    print(*words)