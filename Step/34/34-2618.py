import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
W = int(input())

pos = [[1,1],[N,N]]
for _ in range(W):
    pos.append(list(map(int,input().split())))
dp = [[-1]*(W+2) for _ in range(W+2)]

def cal(i,j):
    if i > W or j > W:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    temp = max(i,j)+1
    ni = cal(temp,j) + abs(pos[temp][0] - pos[i][0]) + abs(pos[temp][1] - pos[i][1])
    nj = cal(i,temp) + abs(pos[temp][0] - pos[j][0]) + abs(pos[temp][1] - pos[j][1])
    dp[i][j] = min(ni,nj)
    return dp[i][j]

def car(i,j):
    if i > W or j > W:
        return
    temp = max(i,j)+1
    ni = abs(pos[temp][0] - pos[i][0]) + abs(pos[temp][1] - pos[i][1])
    nj = abs(pos[temp][0] - pos[j][0]) + abs(pos[temp][1] - pos[j][1])
    
    if dp[temp][j] + ni < dp[i][temp] + nj:
        print(1)
        car(temp,j)
    else:
        print(2)
        car(i,temp)
    return

print(cal(0,1))
car(0,1)