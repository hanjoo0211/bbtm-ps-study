submit = [False for _ in range(30)]
for _ in range(28):
    n = int(input()) - 1
    submit[n] = True
for i in range(30):
    if not submit[i]:
        print(i+1)