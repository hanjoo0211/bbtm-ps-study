s = input()
apbt = [0 for i in range(97, 123)]
for ss in s:
    apbt[ord(ss) - 97] += 1
print(*apbt)