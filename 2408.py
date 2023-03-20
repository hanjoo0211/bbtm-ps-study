n = int(input())
inputs = []
for i in range(2*n-1):
    if i % 2 == 0:
        inputs.append(int(input()))
    else:
        inputs.append(input())

isCombining = True
while isCombining:
    isCombining = False
    for i in range(1, len(inputs), 2):
        if inputs[i] in ['*', '/']:
            if inputs[i] == '*':
                inputs[i-1] *= inputs[i+1]
            elif inputs[i] == '/':
                inputs[i-1] //= inputs[i+1]
            isCombining = True
            inputs.pop(i)
            inputs.pop(i)
            break

s = inputs[0]
for i in range(1, len(inputs), 2):
    if inputs[i] == '+':
        s += inputs[i+1]
    else:
        s -= inputs[i+1]
print(s)