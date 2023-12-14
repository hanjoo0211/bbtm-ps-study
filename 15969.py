n = int(input())
scores = list(map(int, input().split()))
scores.sort()
print(scores[-1] - scores[0])
