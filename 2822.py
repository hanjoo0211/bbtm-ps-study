scores = [(int(input()), i) for i in range(1, 9)]
scores.sort()

answer = 0
questions = []
for score, i in scores[3:]:
    answer += score
    questions.append(i)

questions.sort()
print(answer)
print(*questions)
