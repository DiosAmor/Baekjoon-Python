#pypy
import sys
input = sys.stdin.readline
inf = sys.maxsize

V,E = map(int,input().split())
graph = [[inf]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
result = inf
for i in range(1,V+1):
    if graph[i][i] < result:
        result = graph[i][i]
if result == inf:
    print(-1)
else:
    print(result)