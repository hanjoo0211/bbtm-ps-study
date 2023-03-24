n = int(input())
score = [0, 0, 0]
squareScore = [0, 0, 0]
for _ in range(n):
    s = list(map(int, input().split()))
    for i in range(3):
        score[i] += s[i]
        squareScore[i] += s[i] ** 2

count = 0
maxIndex = 0
maxScore = max(score)
maxSquareScore = max(squareScore)
for i in range(3):
    if squareScore[i] == maxSquareScore:
        count += 1
        maxIndex = i + 1

if count == 1:
    print(maxIndex, maxScore)
else:
    print(0, maxScore)