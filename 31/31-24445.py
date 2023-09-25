from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i].sort(reverse=True)
   
def bfs(node):
    idx = 1
    layer = deque([node])
    visit[node] = idx
    idx+=1
    
    while layer:
        node = layer.popleft()
        for i in graph[node]:
            if visit[i] == 0:
                layer.append(i)
                visit[i] = idx
                idx+=1
bfs(R)
print(*visit[1:],sep="\n")                