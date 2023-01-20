s1, s2 = input(), input()
ss = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            ss[i][j] = ss[i-1][j-1] + 1
        else:
            ss[i][j] = max(ss[i][j-1], ss[i-1][j])
print(ss[-1][-1])