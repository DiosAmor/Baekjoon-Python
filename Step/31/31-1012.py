import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

def dfs(x,y):
    global cnt,N,M
    if x<0 or y<0 or x>M-1 or y>N-1:
        return False
    if cabbage[x][y] == 1:
        cabbage[x][y] = 0
        for i in range(4):
            x_edit = x+dx[i]
            y_edit = y+dy[i]
            dfs(x_edit, y_edit)
        return True
    return False



T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    cabbage = [[0]*N for _ in range(M)]
    for _ in range(K):
        x,y = map(int,input().split())
        cabbage[x][y] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                cnt+=1
    print(cnt)