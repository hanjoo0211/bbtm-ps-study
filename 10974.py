n = int(input())


def bt(perm: list, left: list) -> None:
    if len(perm) == n:
        print(*perm)
        return
    for i in range(len(left)):
        new_perm = perm + [left[i]]
        new_left = left[:i] + left[i+1:]
        bt(new_perm, new_left)


bt([], list(range(1, n+1)))