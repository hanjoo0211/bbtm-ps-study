t = int(input())
for _ in range(t):
    even_sum = 0
    even_min = 100
    nums = list(map(int, input().split()))
    for n in nums:
        if n % 2 == 0:
            even_sum += n
            even_min = min(n, even_min)
    print(even_sum, even_min)