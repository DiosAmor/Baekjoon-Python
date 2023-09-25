from collections import deque
import sys
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(x,y):
    global x_t,y_t,l
    layer = deque([[x,y]])
    
    while layer:
        x,y = layer.popleft()
        if x == x_t and y == y_t:
            return chess[x][y]
        for i in range(8):
            x_edit = x+dx[i]
            y_edit = y+dy[i]
            
            if 0<=x_edit<l and 0<=y_edit<l and not chess[x_edit][y_edit]:
                layer.append([x_edit,y_edit])
                chess[x_edit][y_edit] = chess[x][y] + 1


case = int(input())
for _ in range(case):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    x,y = map(int,input().split())
    x_t,y_t = map(int,input().split())
    print(bfs(x,y))