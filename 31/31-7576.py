from collections import deque
import sys

input = sys.stdin.readline

M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(pos):
    layer = deque(pos)
    while layer:
        x,y = layer.popleft()
        for i in range(4):
            x_edit = x+dx[i]
            y_edit = y+dy[i]
            
            if 0<=x_edit<N and 0<=y_edit<M and box[x_edit][y_edit] == 0:
                layer.append([x_edit,y_edit])
                box[x_edit][y_edit] = box[x][y] + 1

pos = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            pos.append([i,j])
bfs(pos)
cnt = 0
for i in range(N):
    cnt += box[i].count(0)
if cnt > 0:
    print(-1)
else:
    print(max(map(max,box))-1)