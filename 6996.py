t = int(input())
for _ in range(t):
    a, b = input().split()
    a_list, b_list = list(a), list(b)
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
