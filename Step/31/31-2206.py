from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    layer = deque([[x,y,0]])
    while layer:
        x,y,z = layer.popleft()
        if x == N-1 and y == M-1:
            return visit[N-1][M-1][z]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    layer.append([nx,ny,z])
                    
                if graph[nx][ny] == 1 and z == 0:
                    visit[nx][ny][1] = visit[x][y][z] + 1
                    layer.append([nx,ny,1])
    return -1
print(bfs(0,0))