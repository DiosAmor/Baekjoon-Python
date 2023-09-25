import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                
for i in graph[1:]:
    for j in i[1:]:
        if j == inf:
            print(0,end=" ")
        else:
            print(j,end=" ")          
    print()