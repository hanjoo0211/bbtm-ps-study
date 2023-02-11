import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break


def postorder(s: int, e: int) -> None:
    if s > e:
        return None
    else:
        m = e + 1
        for i in range(s+1, e+1):
            if tree[i] > tree[s]:
                m = i
                break
        postorder(s+1, m-1)
        postorder(m, e)
        print(tree[s])


postorder(0, len(tree)-1)