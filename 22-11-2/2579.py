n = int(input())
score = [int(input()) for _ in range(n)]

maxScore = []
for i in range(n):
    if i == 0:
        maxScore.append(score[0])
    elif i == 1:
        maxScore.append(score[0] + score[1])
    elif i == 2:
        s1 = score[0] + score[2]
        s2 = score[1] + score[2]
        if s1 >= s2:
            maxScore.append(s1)
        else:
            maxScore.append(s2)
    else:
            s1 = maxScore[i-2] + score[i]
            s2 = maxScore[i-3] + score[i-1] + score[i]
            if s1 >= s2:
                maxScore.append(s1)
            else:
                maxScore.append(s2)

print(maxScore[n-1])