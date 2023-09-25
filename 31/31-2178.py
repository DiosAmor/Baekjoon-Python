from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    layer = deque([[x,y]])
    while layer:
        x,y = layer.popleft()
        
        for i in range(4):
            x_edit = x+dx[i]
            y_edit = y+dy[i]
            
            if 0<=x_edit<N and 0<=y_edit<M and maze[x_edit][y_edit] == 1:
                layer.append([x_edit,y_edit])
                maze[x_edit][y_edit] = maze[x][y]+1
    return maze[N-1][M-1]
print(bfs(0,0))