import sys
input = sys.stdin.readline

N = int(input())
M = [list(map(int,input().strip())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>N-1 or y>N-1:
        return False
    if M[x][y] == 1:
        cnt += 1
        M[x][y] = 0
        for i in range(4):
            x_edit = x+dx[i]
            y_edit = y+dy[i]
            dfs(x_edit,y_edit)
        return True
    return False

cnt = 0
result = 0
num = []

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            result+=1
            num.append(cnt)
            cnt = 0
num.sort()
print(result)
print(*num,sep="\n")