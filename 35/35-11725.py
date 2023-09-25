import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

Tree = [[] for _ in range(N+1)]
Parent = [0] * (N+1)

for _ in range(N-1):
    u,v = map(int,input().split())
    Tree[u].append(v)
    Tree[v].append(u)
    
def dfs(node):
    for i in Tree[node]:
        if Parent[i] == 0:
            Parent[i] = node
            dfs(i)
            
dfs(1)

for i in range(2,N+1):
    print(Parent[i])