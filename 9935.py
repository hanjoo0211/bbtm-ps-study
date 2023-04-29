string = input()
bomb = input()

stack = []
for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == bomb[-1]:
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
