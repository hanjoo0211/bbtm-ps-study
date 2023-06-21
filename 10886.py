n = int(input())
count = 0
for _ in range(n):
    if int(input()):
        count += 1
    else:
        count -= 1
if count > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")