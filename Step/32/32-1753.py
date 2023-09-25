import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
dis = [int(1e9)]*(V+1)

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

def dij(start):
    dis[start] = 0
    queue = []
    heapq.heappush(queue,[0,start])
    while queue:
        w, node = heapq.heappop(queue)
        
        if dis[node] < w:
            continue
        
        for next_node, next_w in graph[node]:
            distance = w + next_w
            if distance < dis[next_node]:
                dis[next_node] = distance
                heapq.heappush(queue,[distance, next_node])

dij(start)
for i in range(1,V+1):
    if dis[i] == int(1e9):
        print("INF")
    else:
        print(dis[i])
                