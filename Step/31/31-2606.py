import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visit[node] = 1
    for i in graph[node]:
        if visit[i] == 0:
            dfs(i)         
dfs(1)
print(sum(visit)-1)