import sys
input = sys.stdin.readline


while True:
    sentence = list(input())[:-1]
    if sentence == ['.']:
        break
    isYes = True
    wait = [None]
    for st in sentence:
        if st == '(':
            wait.append(')')
        elif st == '[':
            wait.append(']')
        elif st == ')' or st == ']':
            w = wait.pop()
            if st != w:
                isYes = False
                break
    if isYes and wait == [None]:
        print('yes')
    else:
        print('no')