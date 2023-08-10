while True:
    tree = input()
    if tree == "0":
        break
    tree = list(map(int, tree.split()))
    a = tree[0]
    leaves = 1
    for i in range(a):
        leaves *= tree[2*i+1]
        leaves -= tree[2*i+2]
    print(leaves)