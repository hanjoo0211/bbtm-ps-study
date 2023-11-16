t = int(input())
for _ in range(t):
    n = int(input())
    select = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            stack = [i]
            while stack:
                node = stack.pop()
                visited[node] = True
                stack.append(node)
                s = select[node]
                if not visited[s]:
                    stack.append(s)
                else:
                    if s in stack:
                        result += stack[stack.index(s):]
                    break
    print(n - len(result))
