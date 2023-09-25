import sys
input = sys.stdin.readline

tree = {}
N = int(input())
for _ in range(N):
    root, left, right = map(str,input().split())
    tree[root] = [left,right]
    
def preorder(root):
    if root != '.':
        print(root,end="")
        left,right = tree[root]
        preorder(left)
        preorder(right)
def inorder(root):
    if root != '.':
        left,right = tree[root]
        inorder(left)
        print(root,end="")
        inorder(right)
def postorder(root):
    if root != '.':
        left,right = tree[root]
        postorder(left)
        postorder(right)
        print(root,end="")
        
preorder('A')
print()
inorder('A')
print()
postorder('A')