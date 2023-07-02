t = int(input())
for _ in range(t):
    input()
    n = int(input())
    candies = 0
    for _ in range(n):
        candies += int(input())
    if candies % n == 0:
        print("YES")
    else:
        print("NO")