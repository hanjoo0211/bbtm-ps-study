n = int(input())
scores = [int(input()) for _ in range(n)]
count = 0
score = scores[-1]

for i in range(n-2, -1, -1):
    if scores[i] >= score:
        diff = scores[i] - (score - 1)
        count += diff
        scores[i] = score - 1
    score = scores[i]
print(count)
