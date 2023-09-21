score_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
score_sum = 0
credit_sum = 0
for _ in range(20):
    _name, credit, grade = input().split()
    if grade == "P":
        continue
    else:
        score = score_dict[grade]
        score_sum += float(credit) * score
        credit_sum += float(credit)
print(score_sum / credit_sum)