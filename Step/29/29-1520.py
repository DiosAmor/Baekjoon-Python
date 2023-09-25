import sys
input = sys.stdin.readline

M,N = map(int,input().split())
height = []
dp = [[-1]*N for _ in range(M)]

for _ in range(M):
    height.append(list(map(int,input().split())))


def check(x,y):
    if x==M-1 and y==N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    if x>0 and height[x-1][y] < height[x][y]:
        dp[x][y] += check(x-1,y)
    if y>0 and height[x][y-1] < height[x][y]:
        dp[x][y] += check(x,y-1)
    if x<M-1 and height[x+1][y] < height[x][y]:
        dp[x][y] += check(x+1,y)
    if y<N-1 and height[x][y+1] < height[x][y]:
        dp[x][y] += check(x,y+1)
    return dp[x][y]
        
print(check(0,0))
    