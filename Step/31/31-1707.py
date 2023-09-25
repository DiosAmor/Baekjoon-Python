from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    layer = deque([node])
    if visit[node] == 0:
        visit[node] = 1
    while layer:
        node = layer.popleft()
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = visit[node]*(-1)
                layer.append(i)
            elif visit[i] == visit[node]:
                print("NO")
                return False
    return True

K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visit = [0]*(V+1)
    flag = 0
    for i in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for j in range(1,V+1):
        if not bfs(j):
            flag = 1
            break
    if flag == 0:
        print("YES")