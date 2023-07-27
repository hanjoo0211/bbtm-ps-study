n = int(input())
customer = list(map(int, input().split()))
seats = [False for _ in range(101)]
count = 0
for c in customer:
    if seats[c]:
        count += 1
    else:
        seats[c] = True
print(count)