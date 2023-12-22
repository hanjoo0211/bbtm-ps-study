n = int(input())
for _ in range(n):
    num = input()
    l = len(num)
    if num[l // 2 - 1] == num[l // 2]:
        print("Do-it")
    else:
        print("Do-it-Not")
