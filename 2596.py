alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
binary = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
n = int(input())
texts = input()
answer = ''
for i in range(n):
    text = texts[i*6:i*6+6]
    for j in range(8):
        if text == binary[j]:
            answer += alphabet[j]
            break
        for k in range(6):
            typo = text[:k] + str(1-int(text[k])) + text[k+1:]
            if typo == binary[j]:
                answer += alphabet[j]
                break
    if len(answer) != i+1:
        answer = i+1
        break
print(answer)