def quad(n: int, vid: list):
    if n == 1:
        return vid[0][0]
    else:
        q = n // 2
        newVid = []
        newVid.append([v[:q] for v in vid[:q]])
        newVid.append([v[q:] for v in vid[:q]])
        newVid.append([v[:q] for v in vid[q:]])
        newVid.append([v[q:] for v in vid[q:]])
        return [quad(q, newVid[i]) for i in range(4)]


n = int(input())
vid = [list(map(int, list(input()))) for _ in range(n)]
result = str(quad(n, vid)).replace(', ', '').replace('[', '(').replace(']', ')')

isCompressFinish = False
while not isCompressFinish:
    oldLen = len(result)
    result = result.replace('(1111)', '1').replace('(0000)', '0')
    newLen = len(result)
    if oldLen == newLen:
        isCompressFinish = True
print(result)