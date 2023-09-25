n, new_score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    rank = -1
    for i in range(n):
        if new_score > scores[i]:
            rank = i + 1
            break
        elif new_score == scores[i]:
            if n < p:
                rank = i + 1
            elif scores[i] > scores[p-1]:
                rank = i + 1
            break
    if rank == -1 and n < p:
        rank = n + 1
    print(rank)