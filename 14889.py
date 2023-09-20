n = int(input())
tw = [list(map(int, input().split())) for _ in range(n)]
min_diff = 100 * (n ** 2)


def bt(index: int, start: list, link: list) -> None:
    if len(start) == n // 2:
        global min_diff
        start_tw = sum(tw[i][j] for i in start for j in start)
        link_tw = sum(tw[i][j] for i in link for j in link)
        diff = abs(start_tw - link_tw)
        min_diff = min(min_diff, diff)
        return
    for k in range(index, len(link)):
        new_start = start + [link[k]]
        new_link = link[:k] + link[k+1:]
        bt(k, new_start, new_link)


bt(0, [], list(range(n)))
print(min_diff)