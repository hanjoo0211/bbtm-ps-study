import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    score = [(0, 0), (0, 0)]
    for i in range(n):
        s0 = max(score[i][1], score[i+1][1]) + sticker[0][i]
        s1 = max(score[i][0], score[i+1][0]) + sticker[1][i]
        score.append((s0, s1))
    print(max(score[-1]))