def partition(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        return partition(n-1) + partition(n-2) + partition(n-3)


T = int(input())

for _ in range(T):
    num = int(input())
    print(partition(num))