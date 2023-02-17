import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    s = input().rstrip()
    isPalindrome = 1
    recursion = 1
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            recursion += 1
        else:
            isPalindrome = 0
            break
    print(isPalindrome, recursion)