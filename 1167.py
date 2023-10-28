v = int(input())
graph = {}
for _ in range(v):
    line = list(map(int, input().split()))
    for i in range(len(line) - 1):
        if i == 0:
            s = line[i]
        elif i % 2 == 1:
            e = line[i]
        else:
            if graph.get(s):
                graph[s].append((e, line[i]))
            else:
                graph[s] = [(e, line[i])]

stack = [(1, 0)]
visited = [False for _ in range(v+1)]
visited[1] = True
max_node, max_distance = 1, 0
while stack:
    node, distance = stack.pop()
    if distance > max_distance:
        max_node = node
        max_distance = distance
    for new_node, weight in graph[node]:
        if not visited[new_node]:
            visited[new_node] = True
            stack.append((new_node, distance + weight))

stack = [(max_node, 0)]
visited = [False for _ in range(v+1)]
visited[max_node] = True
diameter = 0
while stack:
    node, distance = stack.pop()
    if distance > diameter:
        diameter = distance
    for new_node, weight in graph[node]:
        if not visited[new_node]:
            visited[new_node] = True
            stack.append((new_node, distance + weight))

print(diameter)