import sys

def preorder(root): #전위순회
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root): #중위순회
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root): #후위순회
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')