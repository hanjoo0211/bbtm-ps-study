n = int(input())
paper = [input().split() for _ in range(n)]
count = [0, 0, 0]


def nine(n: int, r: int, c: int):
    num = paper[r][c]
    t = n // 3

    for x in range(r, r + n):
        for y in range(c, c + n):
            if paper[x][y] != num:
                for i in range(3):
                    for j in range(3):
                        nine(t, r + i * t, c + j * t)
                return

    count[int(num)] += 1


nine(n, 0, 0)
for r in range(-1, 2):
    print(count[r])
