n = int(input())
scores = [int(input().replace(".", "")) for _ in range(n)]

for i in range(1, 1001):
    is_dividable = True
    for score in scores:
        j = i * score // 1000 * 1000
        if j // i != score and (j + 1000) // i != score:
            is_dividable = False
            break
    if is_dividable:
        answer = i
        break

print(answer)
