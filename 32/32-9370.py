from heapq import heappop, heappush
import sys
input = sys.stdin.readline
inf = sys.maxsize

def dij(start):
    dis = [inf]*(n+1)
    dis[start] = 0
    heap = []
    heappush(heap,[0,start])
    
    while heap:
        d,node = heappop(heap)
        if dis[node] < d:
            continue
        for next_node,next_d in graph[node]:
            new_d = d+next_d
            if new_d < dis[next_node]:
                dis[next_node] = new_d
                heappush(heap,[new_d,next_node])
    return dis

T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    dij_start = dij(s)
    dij_g = dij(g)
    dij_h = dij(h)
    result = []
    for _ in range(t):
        target = int(input())
        final_dis = min(dij_start[g]+dij_g[h]+dij_h[target],dij_start[h]+dij_h[g]+dij_g[target])
        if final_dis == dij_start[target]:
            result.append(target)
    result.sort()
    print(*result)
    