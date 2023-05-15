n, b = map(int, input().split())
result = []
while n > 0:
    r = n % b
    result.append(r)
    n //= b

result.reverse()
answer = ''
for r in result:
    if r < 10:
        answer += str(r)
    else:
        answer += chr(r+55)
print(answer)