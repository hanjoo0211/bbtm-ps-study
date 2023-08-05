n = int(input())
sell = {}
for _ in range(n):
    book = input()
    if sell.get(book):
        sell[book] += 1
    else:
        sell[book] = 1

maxSell = max(sell.values())
maxSold = []
for book, sells in sell.items():
    if sells == maxSell:
        maxSold.append(book)
maxSold.sort()
print(maxSold[0])