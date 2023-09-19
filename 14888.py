n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
result = []


def bt(i: int, r: int, left_op: list) -> None:
    if i == n:
        result.append(r)
        return
    for j in range(4):
        if left_op[j] > 0:
            if j == 0:
                new_r = r + a[i]
            elif j == 1:
                new_r = r - a[i]
            elif j == 2:
                new_r = r * a[i]
            else:
                if r > 0:
                    new_r = r // a[i]
                else:
                    new_r = -(-r // a[i])
            new_op = left_op.copy()
            new_op[j] -= 1
            bt(i+1, new_r, new_op)


bt(1, a[0], op)
print(max(result))
print(min(result))