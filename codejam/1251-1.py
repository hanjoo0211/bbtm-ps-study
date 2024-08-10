def plus_append(x: str) -> list:
    plus_appended = [x[0]]
    for i in range(1, len(x)):
        new_plus_appended = []
        for r in plus_appended:
            new_plus_appended.append(r + x[i])
            new_plus_appended.append(r + '+' + x[i])
        plus_appended = new_plus_appended
    
    result = []
    for plus_count, plus_string in enumerate(plus_appended):
        s = 0
        num = ""
        for c in plus_string:
            if c == '+':
                s += int(num)
                num = ""
            else:
                num += c
        s += int(num)
        result.append((s, plus_count)) # 계산 결과, '+' 개수를 이진법에서 10진법으로 변환한 값
    return sorted(result, key=lambda x: (x[0], -x[1]))
        

t = int(input())
for _ in range(t):
    n, x = input().split()
    n = int(n)
    v = list(map(int, input().split()))

    result = plus_append(x)
    ws, wp = 0, 0
    for i in v:
        ws += result[i - 1][0]
        plus_count = result[i - 1][1]
        wp += bin(plus_count).count('1')
    print(ws, wp)
