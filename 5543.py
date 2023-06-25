burger, drink = 2000, 2000
for _ in range(3):
    burger = min(burger, int(input()))
for _ in range(2):
    drink = min(drink, int(input()))
print(burger + drink - 50)