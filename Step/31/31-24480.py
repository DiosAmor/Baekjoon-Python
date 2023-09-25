import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i].sort(reverse=True)

idx=1
def dfs(node):
    global idx
    visited[node] = idx
    for i in graph[node]:
        if visited[i] == 0:
            idx += 1
            dfs(i)
dfs(R)
print(*visited[1:],sep="\n")