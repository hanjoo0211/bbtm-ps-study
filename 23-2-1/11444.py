def matMul(a, b):
    r = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                r[i][j] += a[i][k] * b[k][j]
                r[i][j] %= D
    return r


D = 1000000007
n = int(input())
binN = format(n, 'b')

fiboMat = [[[1, 1], [1, 0]]]
for _ in range(len(binN)-1):
    m = matMul(fiboMat[-1], fiboMat[-1])
    fiboMat.append(m)

nMat = [[1, 0], [0, 1]]
for i in range(len(binN)):
    if binN[-i-1] == '1':
        nMat = matMul(fiboMat[i], nMat)
print(nMat[0][1] % D)