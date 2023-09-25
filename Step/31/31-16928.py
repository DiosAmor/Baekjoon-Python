from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
way = [0]*101
visit = [0]*101

for _ in range(N+M):
    u,v = map(int,input().split())
    way[u] = v

def bfs(x):
    layer = deque([x])
    while layer:
        x = layer.popleft()
        if x == 100:
            return visit[x]
        for i in range(1,7):
            if x+i < 101:
                if way[x+i]!=0 and visit[way[x+i]] == 0:
                    layer.append(way[x+i])
                    visit[way[x+i]] = visit[x] + 1
                if way[x+i]==0 and visit[x+i] == 0:
                    layer.append(x+i)
                    visit[x+i] = visit[x] + 1
            
print(bfs(1))