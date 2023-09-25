from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
check_DFS = [0]*(N+1)
check_BFS = [0]*(N+1)
visit_DFS = []
visit_BFS = []

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1,N+1):
    graph[i].sort()

def dfs(node):
    visit_DFS.append(node)
    check_DFS[node] = 1
    for i in graph[node]:
        if check_DFS[i] == 0:
            dfs(i)

def bfs(node):
    layer = deque([node])
    check_BFS[node] = 1
    visit_BFS.append(node)
    while layer:
        node = layer.popleft()
        for i in graph[node]:
            if check_BFS[i] == 0:
                layer.append(i)
                check_BFS[i] = 1
                visit_BFS.append(i)

dfs(R)
bfs(R)
print(*visit_DFS)
print(*visit_BFS)