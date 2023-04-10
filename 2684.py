cases = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']

p = int(input())
for _ in range(p):
    count = [0 for _ in range(8)]
    testcase = input()
    for i in range(38):
        for j in range(8):
            if testcase[i:i+3] == cases[j]:
                count[j] += 1
    for c in count:
        print(c, end=' ')