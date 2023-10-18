scores = [int(input()) for _ in range(10)]
mario = 0
for i in range(10):
    score = sum(scores[:i+1])
    if abs(score - 100) <= abs(mario - 100):
        mario = score
print(mario)