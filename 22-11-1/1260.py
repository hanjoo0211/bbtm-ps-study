from collections import deque


N, M, V = map(int, input().split())

ways = [[] for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    ways[s].append(e)
    ways[e].append(s)


def DFS(V):
    isSearched = []
    toSearch = [V]

    while len(toSearch) > 0:
        c = toSearch.pop()
        ways[c].sort()
        ways[c].reverse()
        for n in ways[c]:
            if n not in isSearched:
                toSearch.append(n)
        if c not in isSearched:
            isSearched.append(c)
    
    result = ''
    for n in isSearched:
        result += str(n) + ' '
    return result[:-1]


def BFS(V):
    isSearched = []
    toSearch = deque([V])

    while toSearch:
        c = toSearch.popleft()
        ways[c].sort()
        for n in ways[c]:
            if n not in isSearched:
                toSearch.append(n)
        if c not in isSearched:
            isSearched.append(c)
    
    result = ''
    for n in isSearched:
        result += str(n) + ' '
    return result[:-1]


print(DFS(V))
print(BFS(V))