n = list(map(int, input().split()))
nn = [i ** 2 for i in n]
print(sum(nn) % 10)