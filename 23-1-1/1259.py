while True:
    num = input()
    if num == '0':
        break
    else:
        isPalindrome = True
        rnum = num[::-1]
        for i in range(len(num)):
            if num[i] != rnum[i]:
                isPalindrome = False
                break
        if isPalindrome:
            print('yes')
        else:
            print('no')