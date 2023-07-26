maxScore = 0
maxIndex = 0
for i in range(5):
    scores = list(map(int, input().split()))
    score = sum(scores)
    if score > maxScore:
        maxIndex = i+1
        maxScore = score
print(maxIndex, maxScore)