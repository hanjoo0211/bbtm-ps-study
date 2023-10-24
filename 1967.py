n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

stack = [(1, 0)]
visited = [False for _ in range(n+1)]
visited[1] = True
max_dist = 0
max_node = 0
while stack:
    node, dist = stack.pop()
    if dist > max_dist:
        max_dist, max_node = dist, node
    for new_node, weight in tree[node]:
        if not visited[new_node]:
            visited[new_node] = True
            stack.append((new_node, dist + weight))

stack = [(max_node, 0)]
visited = [False for _ in range(n+1)]
visited[max_node] = True
max_dist = 0
while stack:
    node, dist = stack.pop()
    if dist > max_dist:
        max_dist = dist
    for new_node, weight in tree[node]:
        if not visited[new_node]:
            visited[new_node] = True
            stack.append((new_node, dist + weight))

print(max_dist)