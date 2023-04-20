n = int(input())
score = 0
totalCredit = 0
for _ in range(n):
    name, credit, grade = input().split()
    credit = int(credit)
    if grade == 'A+':
        score += credit * 4.3
    elif grade == 'A0':
        score += credit * 4.0
    elif grade == 'A-':
        score += credit * 3.7
    elif grade == 'B+':
        score += credit * 3.3
    elif grade == 'B0':
        score += credit * 3.0
    elif grade == 'B-':
        score += credit * 2.7
    elif grade == 'C+':
        score += credit * 2.3
    elif grade == 'C0':
        score += credit * 2.0
    elif grade == 'C-':
        score += credit * 1.7
    elif grade == 'D+':
        score += credit * 1.3
    elif grade == 'D0':
        score += credit * 1.0
    elif grade == 'D-':
        score += credit * 0.7
    totalCredit += credit
finalScore = (score / totalCredit + 0.005) * 100 // 1 / 100
print("%.2f" % (finalScore))