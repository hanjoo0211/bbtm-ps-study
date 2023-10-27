d, h, w = map(int, input().split())
x = (d ** 2 / (w ** 2 + h ** 2)) ** (1/2)
print(int(h * x), int(w * x))