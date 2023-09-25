from collections import deque
import sys
input = sys.stdin.readline

M,N,H = map(int,input().split())

box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

def bfs(pos):
    layer = deque(pos)
    while layer:
        x,y,z = layer.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and box[nx][ny][nz] == 0:
                layer.append([nx,ny,nz])
                box[nx][ny][nz] = box[x][y][z] + 1
pos = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                pos.append([i,j,k])
                
bfs(pos)
cnt = 0
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                cnt = 1
                break
            if box[i][j][k] > result:
                result = box[i][j][k]
                
if cnt > 0:
    print(-1)
else:
    print(result-1)