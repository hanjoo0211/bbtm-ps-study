n = int(input())
answer = list(map(int, input().split()))
score = 0
c = 0
for a in answer:
    if a == 1:
        c += 1
    else:
        c = 0
    score += c
print(score)