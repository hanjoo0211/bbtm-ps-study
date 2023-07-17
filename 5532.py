import math

l, a, b, c, d = int(input()), int(input()), int(input()), int(input()), int(input())
print(l - math.ceil(max(a/c, b/d)))