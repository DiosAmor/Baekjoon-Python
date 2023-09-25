import sys
import heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int,input().split())

def dij(start):
    dis = [INF]*(N+1)
    dis[start] = 0
    queue = []
    heapq.heappush(queue,[0,start])
    while queue:
        w,node = heapq.heappop(queue)
        if dis[node] < w:
            continue
        for next_node,next_w in graph[node]:
            new_dis = w+next_w
            if new_dis < dis[next_node]:
                dis[next_node] = new_dis
                heapq.heappush(queue,[new_dis,next_node])
    return dis

dij_start = dij(1)
dij_v1 = dij(v1)
dij_v2 = dij(v2)
result = min(dij_start[v1]+dij_v1[v2]+dij_v2[N], dij_start[v2]+dij_v1[N]+dij_v2[v1])
print(result if result < INF else -1)