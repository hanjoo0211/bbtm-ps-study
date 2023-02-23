class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n = int(input())
nodes = [Node(chr(i+65)) for i in range(26)]
for _ in range(n):
    d, l, r = input().split()
    node = nodes[ord(d)-65]
    if l != '.':
        node.left = nodes[ord(l)-65]
    if r != '.':
        node.right = nodes[ord(r)-65]

preorderString = ''
def preorder(node: Node) -> None:
    global preorderString
    if node:
        preorderString += node.data
        preorder(node.left)
        preorder(node.right)

inorderString = ''
def inorder(node: Node) -> None:
    global inorderString
    if node:
        inorder(node.left)
        inorderString += node.data
        inorder(node.right)

postorderString = ''
def postorder(node: Node) -> None:
    global postorderString
    if node:
        postorder(node.left)
        postorder(node.right)
        postorderString += node.data

preorder(nodes[0])
print(preorderString)
inorder(nodes[0])
print(inorderString)
postorder(nodes[0])
print(postorderString)