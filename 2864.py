a, b = input().split()
a_six, b_six = a.replace("5", "6"), b.replace("5", "6")
a_five, b_five = a.replace("6", "5"), b.replace("6", "5")
print(int(a_five) + int(b_five), int(a_six) + int(b_six))
