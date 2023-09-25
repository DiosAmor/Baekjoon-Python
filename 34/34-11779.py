from heapq import heappop, heappush
import sys
inf = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())

dis = [inf]*(n+1)
stamp = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
start,stop = map(int,input().split())

def dij(start):
    heap = []
    dis[start] = 0
    heappush(heap,[0,start])
    while heap:
        distance,node = heappop(heap)
        if distance > dis[node]:
            continue
        for next_node, c in graph[node]:
            new_dis = distance + c
            if new_dis < dis[next_node]:
                dis[next_node] = new_dis
                heappush(heap,[new_dis,next_node])
                stamp[next_node] = node
dij(start)
print(dis[stop])
city = []
temp = stop
while True:
    city.append(temp)
    if temp == start:
        break
    temp = stamp[temp]
city.reverse()
print(len(city))
print(*city)
                