n = int(input())
solutions = list(map(int, input().split()))

i, j = 0, n - 1
min_s = 2000000000
min_i, min_j = None, None
while i < j:
    s = solutions[i] + solutions[j]
    if abs(s) < min_s:
        min_s = abs(s)
        min_i, min_j = i, j
    if s < 0:
        i += 1
    elif s > 0:
        j -= 1
    else:
        break
print(solutions[min_i], solutions[min_j])
