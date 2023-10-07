t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    if n > 32:
        print(0)
    else:
        min_dist = 13
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    dist = 0
                    for l in range(4):
                        if mbti[i][l] != mbti[j][l]:
                            dist += 1
                        if mbti[j][l] != mbti[k][l]:
                            dist += 1
                        if mbti[k][l] != mbti[i][l]:
                            dist += 1
                    min_dist = min(min_dist, dist)
        print(min_dist)