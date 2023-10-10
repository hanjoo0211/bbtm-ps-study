tc = int(input())
for _ in range(tc):
    is_rewind = False
    n, m, w = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    worms = [tuple(map(int, input().split())) for _ in range(w)]
    graph = [[10001 for _ in range(n+1)] for _ in range(n+1)]
    for s, e, t in roads:
        graph[s][e] = min(t, graph[s][e])
        graph[e][s] = min(t, graph[e][s])
    for s, e, t in worms:
        graph[s][e] = min(-t, graph[s][e])

    for i in range(1, n+1):
        if is_rewind:
            break
        for j in range(1, n+1):
            if is_rewind:
                break
            for k in range(1, n+1):
                new_edge = graph[j][i] + graph[i][k]
                if new_edge < graph[j][k]:
                    graph[j][k] = new_edge
                    if j == k and graph[j][k] < 0:
                        is_rewind = True
                        break
    print("YES") if is_rewind else print("NO")
