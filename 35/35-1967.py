import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node,cost):
    for i,j in tree[node]:
        if visit[i] == 0:
            visit[i] = j+cost
            dfs(i,j+cost)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,c = map(int,input().split())
    tree[u].append([v,c])
    tree[v].append([u,c])
    
visit = [0] * (n+1)
visit[1] = -1
dfs(1,0)

start = visit.index(max(visit))
visit = [0] * (n+1)
visit[start] = -1
dfs(start,0)
print(max(visit))