n = int(input())
words = [input() for _ in range(n)]

wordDict = {}
for word in words:
    for i in range(len(word)):
        char = word[i]
        if wordDict.get(char):
            wordDict[char] += 10 ** (len(word)-i-1)
        else:
            wordDict[char] = 10 ** (len(word)-i-1)

maxSum = 0
wordTuple = sorted(wordDict.items(), key=lambda x:x[1])
for i, (char, value) in enumerate(reversed(wordTuple)):
    maxSum += (9-i) * value

print(maxSum)