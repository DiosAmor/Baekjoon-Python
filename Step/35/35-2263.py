import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

tree = [0]*(n+1)
for i in range(n):
    tree[inorder[i]] = i
    
def preorder(inStart,inEnd,poStart,poEnd):
    if inStart > inEnd or poStart > poEnd:
        return
    root = postorder[poEnd]
    
    leftTree = tree[root] - inStart
    rightTree = inEnd - tree[root]
    
    print(root,end=" ")
    preorder(inStart,inStart+leftTree-1,poStart,poStart+leftTree-1)
    preorder(inEnd-rightTree+1,inEnd,poEnd-rightTree,poEnd-1)
    
preorder(0,n-1,0,n-1)